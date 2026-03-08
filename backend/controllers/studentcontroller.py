from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import getConnection
from models.models import Students

router = APIRouter(prefix="/api")

@router.get("/getall")
def getall(db: Session = Depends(getConnection)):
    studentsdata = db.query(Students).all()
    
    return {"data": [
            {"id": s.id, "firstname": s.firstname, "lastname": s.lastname, "phone": s.phone, "emailid": s.emailid}
            for s in studentsdata
        ]
    }