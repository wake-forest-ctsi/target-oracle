from singer_sdk import typing as th

target_config = th.PropertiesList(
    th.Property("drivername", th.StringType, required=False, description="the name of the database backend. This name will correspond to a module in sqlalchemy/databases or a third party plug-in.", default="oracle+cx_oracle"),
    th.Property("username", th.StringType, required=False, description="The user name"),
    th.Property("password", th.StringType, required=False, description="database password"),
    th.Property("host", th.StringType, required=False, description="The name of the host"),
    th.Property("port", th.IntegerType, required=False, description="The port number", default=1521),
    th.Property("database", th.StringType, required=False, description="The database name"),
    # th.Property("query", ?, required=False, description="A dictionary of string keys to string values to be passed to the dialect and/or the DBAPI upon connect"),
    th.Property("add_record_metadata", th.BooleanType, description="Enables integration _sdc_ columns at the target", default=False),
    th.Property("sqlalchemy_url", th.StringType, description="SQLAlchemy connection string", default=False),
)

__all__ = ["target_config"]