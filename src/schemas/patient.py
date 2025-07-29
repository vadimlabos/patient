from typing import Optional

from pydantic import BaseModel


class PatientSchema(BaseModel):
    icode: int
    itz: str
    ilast: str
    ifirst: str
    ifather: str
    idob: Optional[int] = None
    isex: Optional[int] = None
    istr1: str
    istr2: str
    izip: str
    iphone: str
    ifax: str
    itype: Optional[int] = None
    idate: Optional[int] = None
    idept: Optional[int] = None
    icredit: Optional[int] = None
    ihiv: Optional[int] = None
    isrce: Optional[int] = None
    iacc: str
    ihpb: Optional[int] = None
    isndcode: Optional[int] = None
    iheight: Optional[int] = None
    iweight: Optional[float] = None
    istate: Optional[int] = None
    iroom: str
    iorigland: Optional[int] = None
    iisdead: Optional[int] = None
    ipopultype: Optional[int] = None
    iprofession: Optional[int] = None
    iemploydate: Optional[int] = None
    iidtype: int
    imosrce2: Optional[int] = None
    imosrce1: Optional[int] = None
    ifasrce2: Optional[int] = None
    ifasrce1: Optional[int] = None
    iwphone1: str
    iphoneext: Optional[int] = None
    imobile: str
    iemail: str
    ibeeper: Optional[int] = None
    iotherid1: str
    iotherid2: str
    idoccode: Optional[int] = None
    ipersonal: Optional[int] = None
    icity: Optional[int] = None
    icountry: Optional[int] = None
    istr3: str
    idateofdeath: Optional[int] = None
    iselfpay: Optional[int] = None
    imid: str
    ielastname: str
    iefirstname: str
    ieid: str
    iestr1: str
    iestr2: str
    iestr3: str
    iezip: str
    iestate: Optional[int] = None
    iecity: Optional[int] = None
    iecountry: Optional[int] = None
    iemobile: str
    iebeeper: Optional[int] = None
    ieemail: str
    iephone: str
    iephoneext: Optional[int] = None
    iewphone1: str
    iefax: str
    iref: str
    iid: str
    inocharge: Optional[int] = None
    lastupdate: Optional[int] = None
    icityn: str
    iecityn: str
    istatus: Optional[int] = None
    ibloodtype: str
    istudycode: Optional[int] = None
    isstr1: str
    isstr2: str
    iszip: str
    iscity: Optional[int] = None
    iscityn: str
    isstate: Optional[int] = None
    iscountry: Optional[int] = None
    isphone: str
    ismobile: str
    iviewresultdist: Optional[int] = None
    ivip: Optional[int] = None

    class Config:
        from_attributes = True
