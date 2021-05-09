# LookerScripts



**Welcome**

Please read these before using scripts in this repository: 
- **The Support Team does NOT support these scripts**. These are scripts written, collected, or adapted by me **personally** and are not guaranteed or waranteed by Looker / GCP in any way. **Please do not** contact Looker Support about these scripts. Instead consider posting in the [community](https://community.looker.com) or open an issue on this repository 
- These scripts are not regularly tested, and may be out of date with later versions of Looker.
- Python scripts heavily use the `looker_sdk` and `pandas`
- Unless explicitely mentioned in a script's README, download scripts do not support dashboards that use merged results tiles. 

**Python Scripts**


- `DownloadMultiTileTabbed` - Downloads a singular dashboard with any number of tiles as a Tabbed Excel file
- `DownloadMultiLookTabbed` - Downloads any number of Looks as a single Tabbed Excel file
- `DownloadDashboardUnlimited` - Downloads unlimited results from a singular dashboard with any number of tiles as a Tabbed Excel file. 
- `DownloadDifferentDelimiter` - Downloads `csv`s with a custom delimiter
- `DownloadCSVorExcel` - Downloads a dashboard as a series of either `csv` or `xlsx` files instead of the default `csv_zip`
- `DownloadUnlimitedMergedv1` - Downloads unlimited results from a merged results dashboard tile, as a set of `csv` files (one for each merged query). 
- `DownloadUnlimitedMergedv2` - Downloads unlimited results from a merged results dashboard tile, as *a single CSV with merged queries joined*. This has limitations, see notes in script.

**JS / Sheet Scripts**

- `GoogleSheets_AutoRefresh` - Similar to the Sheets Looker Action. Imports data from a Look into a Google Sheet and pulls new data each time the sheet is opened. Note: Last tested 12/2019
