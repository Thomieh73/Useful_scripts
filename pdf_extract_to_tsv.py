import camelot
import pandas as pd
import argparse
import os

# This script was created using google gemini
# --- Configuration ---
# The extraction method will be 'lattice' (best for tables with clear lines)
FLAVOR = 'lattice'

def extract_and_combine_tables(pdf_path, page_range):
    """
    Extracts tables from a specified page range of a PDF using Camelot's 'lattice' mode 
    and combines them into a single pandas DataFrame.
    """
    if not os.path.exists(pdf_path):
        print(f"!!! Error: PDF file not found at path: {pdf_path}")
        return None

    print(f"--- Starting extraction from: {pdf_path} (Pages: {page_range})...")
    
    try:
        # Use 'lattice' flavor (as requested)
        tables = camelot.read_pdf(
            pdf_path, 
            pages=page_range, 
            flavor=FLAVOR
        )

        if not tables:
            print("!!! No tables were detected by Camelot.")
            return None

        print(f"*** Successfully detected {tables.n} tables across the specified pages.")
        
        dataframes = []
        for i, table in enumerate(tables):
            df = table.df
            # Display page number(s) where the table was found
            print(f"   - Table from page(s) {table.page} has {len(df)} rows.") 
            dataframes.append(df)
            
        # Combine all DataFrames into a single one (stacks them vertically)
        combined_df = pd.concat(dataframes, ignore_index=True)
        
        # --- Clean up the Header (Assuming a single-row header is extracted) ---
        # 1. Use the first row as the column headers
        combined_df.columns = combined_df.iloc[0]
        
        # 2. Remove the header row that was just used for the column names
        combined_df = combined_df[1:].reset_index(drop=True)
        
        # 3. Drop any rows that exactly match the header (repeated headers on subsequent pages)
        header_row = list(combined_df.columns)
        is_header_repeat = (combined_df == header_row).all(axis=1)
        combined_df = combined_df[~is_header_repeat].reset_index(drop=True)
        
        return combined_df

    except Exception as e:
        print(f"An error occurred during extraction: {e}")
        return None

# --- Main Execution ---
if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(
        description="Extracts multi-page tables from a PDF using Camelot and saves them to a CSV file.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "pdf_file_path", 
        help="The path to the input PDF file (e.g., 'data/report.pdf')."
    )
    parser.add_argument(
        "page_range", 
        help=(
            "The page range where the table is spread (e.g., '3' for page 3, "
            "'1-5' for pages 1 through 5, or '1,3,5' for specific pages)."
        )
    )
    
    args = parser.parse_args()
    
    # Run the extraction function with arguments provided by the user
    final_table = extract_and_combine_tables(args.pdf_file_path, args.page_range)

    if final_table is not None:
        try:
            # --- NEW CLEANUP STEP HERE ---
            # Apply a string replacement to all cells in the DataFrame
            # to remove newline characters ('\n') and carriage returns ('\r').
            # We replace them with a space to keep multi-line words separated.
            final_table = final_table.replace({'\n': ' '}, regex=True)
            final_table = final_table.replace({'\r': ' '}, regex=True)
            
            # Now, the DataFrame is clean and ready to save
            base_name = os.path.splitext(os.path.basename(args.pdf_file_path))[0]
            output_name = f"{base_name}_extracted_table.tsv"
            
            # Save the final combined DataFrame to a CSV file
            final_table.to_csv(output_name, index=False, sep='\t', encoding='utf-8')
            
            print(f"\n*** Success! Combined table saved to: {os.path.abspath(output_name)}")
            print(f"Total rows extracted (excluding header): {len(final_table)}")
            
        except Exception as e:
            print(f"!!! Error saving to CSV: {e}")
