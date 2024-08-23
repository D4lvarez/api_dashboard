from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    password: str
    is_deleted: bool = Field(default=False, index=True)

    # Relations
    tenable_reports: list["TenableReport"] = Relationship(back_populates="created_by")
    tenasus_reports: list["TenasusReport"] = Relationship(back_populates="created_by")


class Client(SQLModel, table=True):
    __tablename__ = "clients"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)

    # Relations
    tenable_reports: list["TenableReport"] = Relationship(back_populates="client")
    tenasus_reports: list["TenasusReport"] = Relationship(back_populates="created_by")


class TenableReport(SQLModel, table=True):
    __tablename__ = "tenable_reports"
    id: int | None = Field(default=None, primary_key=True)
    target: str
    targeted_at: datetime
    created_at: datetime

    # Relations
    client_id: int = Field(foreign_key="clients.id")
    client: Client = Relationship(back_populates="tenable_reports")
    created_by_id: int = Field(foreign_key="users.id")
    created_by: User = Relationship(back_populates="tenable_reports")

    details: list["TenableDetail"] = Relationship(back_populates="tenable_report")


class TenableDetail(SQLModel, table=True):
    __tablename__ = "tenable_details"
    id: int | None = Field(default=None, primary_key=True)
    severity: str
    cvss: str
    vpr: str
    plugin: str
    name: str
    url: str

    # Relations
    tenable_report_id: int = Field(foreign_key="tenable_reports.id")
    tenable_report: TenableReport = Relationship(back_populates="details")


class TenasusReport(SQLModel, table=True):
    __tablename__ = "tenasus_reports"
    id: int | None = Field(default=None, primary_key=True)
    target: str
    targeted_at: datetime
    created_at: datetime

    # Relations
    client_id: int = Field(foreign_key="clients.id")
    client: Client = Relationship(back_populates="tenasus_reports")
    created_by_id: int = Field(foreign_key="users.id")
    created_by: User = Relationship(back_populates="tenasus_reports")

    summary: list["TenasusSummary"] = Relationship(back_populates="tenasus_report")
    alerts: list["TenasusAlerts"] = Relationship(back_populates="tenasus_report")
    details: list["TenasusDetail"] = Relationship(back_populates="tenasus_report")


class TenasusSummary(SQLModel, table=True):
    __tablename__ = "tenasus_reports_summary"
    id: int | None = Field(default=None, primary_key=True)
    risk_level: str
    alert_instances: int

    # Relations
    tenasus_report_id: int = Field(foreign_key="tenasus_reports.id")
    tenasus_report: TenasusReport = Relationship(back_populates="summary")


class TenasusAlerts(SQLModel, table=True):
    __tablename__ = "tenasus_reports_alerts"
    id: int | None = Field(default=None, primary_key=True)
    vulnerability_name: str
    level: str
    instances: int

    # Relations
    tenasus_report_id: int = Field(foreign_key="tenasus_reports.id")
    tenasus_report: TenasusReport = Relationship(back_populates="alerts")


class TenasusDetail(SQLModel, table=True):
    __tablename__ = "tenasus_reports_details"
    id: int | None = Field(default=None, primary_key=True)
    vulnerability_name: str
    description: str
    risk_level: str
    instances: int
    solution: str
    other_info: str
    reference: str
    cwe_id: int | None = Field(default=None)
    wasc_id: int | None = Field(default=None)
    source_id: int | None = Field(default=None)

    # Relations
    tenasus_report_id: int = Field(foreign_key="tenasus_reports.id")
    tenasus_report: TenasusReport = Relationship(back_populates="details")
    locations: list["TenasusLocations"] = Relationship(back_populates="tenasus_detail")


class TenasusLocations(SQLModel, table=True):
    __tablename__ = "tenasus_report_details_location"
    id: int | None = Field(default=None, primary_key=True)
    url: str
    method: str
    evidence: str | None = Field(default=None)
    parameter: str | None = Field(default=None)

    # Relations
    tenasus_report_detail_id: int = Field(foreign_key="tenasus_reports_details.id")
    tenasus_detail: TenasusDetail = Relationship(back_populates="locations")
