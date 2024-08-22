from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship


class TenableReport(SQLModel, table=True):
    __tablename__ = "tenable_reports"
    id: int | None = Field(default=None, primary_key=True)
    target: str
    targeted_at: datetime
    created_at: datetime

    # Relations
    details: "TenableDetail" = Relationship(back_populates="tenable_report")


class TenableDetail(SQLModel, table=True):
    __tablename__ = "tenable_details"
    id: int | None = Field(default=None, primary_key=True)
    severity: str
    cvss: int | str
    vpr: int | str
    plugin: int | str
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
    __tablename__ = ""
    id: int | None = Field(default=None, primary_key=True)
    url: str
    method: str
    evidence: str | None = Field(default=None)
    parameter: str | None = Field(default=None)

    # Relations
    tenasus_report_detail_id: int = Field(foreign_key="tenasus_reports_details.id")
    tenasus_detail: TenasusDetail = Relationship(back_populates="locations")
