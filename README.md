# GX GitHub Issues validation

Set `GX_MYSQL_CONNECTION_STRING` before running the validation. The value should be a SQLAlchemy MySQL URL for the `github_issues` database. The connection string is read from the environment by both the Python setup and Great Expectations configuration.

PowerShell example:

```powershell
$env:GX_MYSQL_CONNECTION_STRING = "mysql+pymysql://<user>:<password>@localhost:3306/github_issues"
python main.py
```
