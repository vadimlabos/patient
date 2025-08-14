from typing import Optional

from pydantic import BaseModel, ConfigDict


class RequestSchema(BaseModel):
    rordno: int
    rdate: int
    rlabel: int
    rtest: int
    rinst: Optional[int]
    rstatus: Optional[int]
    rlab: Optional[int]
    rresult: Optional[str]
    rcommconst: Optional[int]
    rcommfree: Optional[int]
    rappdat: Optional[int]
    rapptim: Optional[int]
    rbounds: Optional[int]
    rrerun: Optional[int]
    rinprof: Optional[int]
    rphinst: Optional[int]
    ruser: Optional[int]
    rdelta: Optional[int]
    rlocation: Optional[int]
    rtubenum: int
    rdynamictime: Optional[int]
    rrun: Optional[int]
    rtray: Optional[int]
    rdilution: Optional[float]
    rresstat: Optional[int]
    risreruns: Optional[int]
    rflag: Optional[int]
    rsort: Optional[int]
    rpreresult: Optional[str]
    rgraph: Optional[int]
    rprint: Optional[int]
    rlaststatus: Optional[int]
    rprevtestalert: Optional[int]
    rcommrunconst: Optional[int]
    rcommrunfree: Optional[int]
    rformulainfo: Optional[str]
    rurgent: Optional[int]
    rqcstatus: Optional[int]
    ralert: Optional[int]
    rautobounds: Optional[int]
    rtestnum: int
    rorigtest: Optional[int]
    runique: int
    rtechapp: Optional[int]
    rparam: Optional[int]
    rcount: Optional[int]
    rhead: Optional[int]
    rprnsort: Optional[int]
    rprofnum: Optional[int]
    rhasdist: Optional[int]
    rperformsite: Optional[int]
    rinsertdate: Optional[int]
    rinserttime: Optional[int]
    risprofile: Optional[int]
    rphonedist: Optional[int]
    rnumresult: Optional[float]
    rbillcount: Optional[int]
    rdiffdist: Optional[int]
    rboundsvalue: Optional[str]
    rmnstatus: Optional[int]
    risreject: Optional[int]
    runits: Optional[int]
    rparam2: Optional[int]
    rquantity: Optional[float]
    ronhold: Optional[int]
    roverdue: Optional[int]
    rmainpanel: Optional[int]

    model_config = ConfigDict(from_attributes=True)
