from singer_sdk import typing as th

target_config = th.PropertiesList(
    th.Property("drivername", th.StringType, required=True, description="the name of the database backend. This name will correspond to a module in sqlalchemy/databases or a third party plug-in."),
    th.Property("username", th.StringType, required=True, description="The user name"),
    th.Property("password", th.StringType, required=True, description="database password"),
    th.Property("host", th.StringType, required=True, description="The name of the host"),
    th.Property("port", th.StringType, required=True, description="The port number"),
    th.Property("database", th.StringType, required=True, description="The database name"),
    # th.Property("query", ?, required=False, description="A dictionary of string keys to string values to be passed to the dialect and/or the DBAPI upon connect"),
)

__all__ = ["target_config"]