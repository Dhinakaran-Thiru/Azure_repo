# Azure_repo
Data Lake Setup:

Step 1: Create Container in ADLS

Create a container in Azure Data Lake Storage (ADLS) named sales_view_devtst.

Step 2: Create Folders and Upload Files

Within the sales_view_devtst container, create the following folders:

customer
product
store
sales
Upload files into each folder in the following sequence for real-time functionality.

ADF Pipeline Setup:

Step 1: Create ADF Pipeline

Create an Azure Data Factory (ADF) pipeline to retrieve the latest modified files from the folders in ADLS.

Step 2: Parameterize the Pipeline

Parameterize the pipeline to enable dynamic functionality. Parameters should facilitate the processing of files for any day.

Bronze Layer Setup:

Step 1: Create Bronze Container

Create a container in ADLS named Bronze/sales_view/.

Step 2: Copy Raw Data from ADF Pipeline

Copy raw data from the ADF pipeline to the respective subfolders (customer, product, store, sales) within the Bronze/sales_view/ container.

Silver Layer Transformation:

Customer File Transformation:

Convert all column headers to snake case in lower case.
Split the "Name" column into "first_name" and "last_name".
Extract the domain from the email column.
Assign gender based on "M" or "F".
Split Joining date into date and time.
Format date column to "yyyy-MM-dd".
Assign "expenditure-status" based on the spent column.
Write data to silver layer [table_name: customer].
Product File Transformation:

Convert column headers to snake case in lower case.
Create a "sub_category" column based on category_id.
Write data to silver layer [table_name: product].
Store File Transformation:

Convert column headers to snake case in lower case.
Create a "store category" column from the email.
Format created_at and updated_at to "yyyy-MM-dd".
Write data to silver layer [table_name: store].
Sales File Transformation:

Convert column headers to snake case in lower case.
Write data to silver layer [table_name: customer_sales].
Gold Layer Analysis:

Retrieve data using Product and Store Tables

Step 1: Retrieve Data

Retrieve data using the product and store tables.

Step 2: Get Specific Data Fields

Get specific data fields from the customer_sales table.

Step 3: Write Data to Gold Layer

Write data to the gold layer [table_name: StoreProductSalesAnalysis].

Note: All dates should be maintained in "yyyy-MM-dd" format.

File Paths:

Silver Layer:

silver/sales_view/tablename/{delta parquet}
Gold Layer:

gold/sales_view/tablename/{delta parquet}
