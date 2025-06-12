import pandas as pd
import numpy as np

from utils.StratifierCommonFunctions import print_distribution, compute_target_counts, compute_distribution_by_sum_perc, \
    compute_distribution_by_sum_counts, log_progress


class StratifierKnapsack:

    def __init__(self, use_relevance_score=False, debug=False):
        self.use_relevance_score = use_relevance_score
        self.debug = debug

    def stratify(self,df, DIM, M):
        if self.debug: print("Initial Dataset Distribution:")


        distribution_perc = compute_distribution_by_sum_perc(df, DIM)


        # Define target counts based on calculated distribution
        target_counts = compute_target_counts(distribution_perc, DIM, M)

        if self.debug: print(f"target_counts = {target_counts}")

        if self.use_relevance_score:
            df_sorted = df.sort_values(by='relevance_score', ascending=False)
        else:
            # Step 1: Calculate combined scores for each row
            df['score'] = 0
            for classes in DIM:
                num_classes = len(classes)
                max_variance = (num_classes - 1) / (num_classes ** 2)

                # Calculate confidence
                class_probs = df[classes].values
                actual_variance = np.var(class_probs, axis=1)
                confidence = np.clip(actual_variance / max_variance, 0, 1)
                df['score'] += confidence

            df['score'] /= len(DIM)

            # Step 2: Sort rows by score in descending order
            df_sorted = df.sort_values(by='score', ascending=False)

        # Step 3: Greedy selection with constraint checking
        selected_sample = []
        current_counts = {cls: 0 for dim in DIM for cls in dim}
        i = 0

        for idx, row in df_sorted.iterrows():
            valid = True
            i += 1

            selected_classes = {}
            for dim_index, classes in enumerate(DIM):
                max_class = max(classes, key=lambda cls: row.get(cls, 0))
                if current_counts[max_class] < target_counts[max_class]:
                    selected_classes[max_class] = True
                else:
                    valid = False
                    break

            if valid:
                #log_progress(len(selected_sample), M)
                selected_sample.append(row)

                for cls in selected_classes.keys():
                    current_counts[cls] += 1

            if len(selected_sample) == M:
                break


        # Convert selected samples to DataFrame
        sample_df = pd.DataFrame(selected_sample)

        # Final Adjustment: Add or remove reviews to meet the exact sample size
        if len(sample_df) < M:
            # Add reviews with the next highest confidence scores
            remaining_rows = df_sorted.loc[~df_sorted.index.isin(sample_df.index)]
            for idx, row in remaining_rows.iterrows():
                sample_df = pd.concat([sample_df, pd.DataFrame([row])])
                if len(sample_df) == M:
                    break

        elif len(sample_df) > M:
            # Remove reviews with the lowest confidence scores
            sample_df = sample_df.sort_values(by='score', ascending=False).head(M)

        # Ensure the class distributions remain approximately consistent
        final_distribution = compute_distribution_by_sum_perc(sample_df, DIM)
        if self.debug:
            print("Final Sample Distribution:")
            print_distribution(final_distribution)

        return sample_df








