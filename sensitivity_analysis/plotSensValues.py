import pickle
import matplotlib.pyplot as plt
import sys
import os
from typing import Dict, List

# Append the project root to sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(project_root, '..')
sys.path.append(project_root)
from definitions.constants import SENSITIVITY_DIR, SENS_PARAMETER_CONFIG

def load_pickle(file_path: str) -> Dict:
    with open(file_path, 'rb') as file:
        return pickle.load(file)

def plot_group(parameter: str, metrics: Dict[str, tuple], output_path: str) -> None:
    fig, axs = plt.subplots(len(metrics), 1, figsize=(10, 6 * len(metrics)))
    if len(metrics) == 1:
        axs = [axs]

    for ax, (metric_key, (title, y_label, color)) in zip(axs, metrics.items()):
        full_metric_name = f"{metric_key}_{parameter}"
        data = load_pickle(os.path.join(SENSITIVITY_DIR, f"{full_metric_name}.pkl"))
        
        # Special handling for list-type parameters
        if parameter in ['mom_window', 'half_life']:
            # Convert string keys like '[252]' to integers and sort
            processed = []
            for k, v in data.items():
                try:
                    # Remove brackets and convert to integer
                    num_val = int(k.strip('[]'))
                    processed.append((num_val, k, v))
                except:
                    processed.append((float('inf'), k, v))
            
            # Sort by numeric value while keeping original string key
            processed.sort(key=lambda x: x[0])
            sorted_keys = [str(p[0]) for p in processed]  # Use numeric value as label
            sorted_values = [p[2] for p in processed]
        else:
            # Standard numeric sorting for other parameters
            try:
                keys = [float(k) if '.' in k else int(k) for k in data.keys()]
            except:
                keys = list(data.keys())
            
            values = list(data.values())
            sorted_pairs = sorted(zip(keys, values), key=lambda x: x[0])
            sorted_keys, sorted_values = zip(*sorted_pairs) if sorted_pairs else ([], [])

        ax.plot(sorted_keys, sorted_values, marker='o', color=color)
        ax.set_title(title)
        ax.set_xlabel(parameter.replace('_', ' ').title())
        ax.set_ylabel(y_label)
        
        # Improve x-axis labels for list-type parameters
        if parameter in ['mom_window', 'half_life']:
            ax.set_xticks(sorted_keys)
            ax.set_xticklabels([str(p[0]) for p in processed])  # Show numeric values

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Plot group saved to {output_path}")

# Generate plots
for parameter, metrics in SENS_PARAMETER_CONFIG.items():
    output_path = f"{parameter}_sensitivity_analysis.pdf"
    plot_group(parameter, metrics, output_path)