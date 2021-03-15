# dataaccess\requestDataAccess.py
from entities.request import Request, RequestSchema
from entities.databaseSessionManager import SessionManager
from models.defaultMethodResult import DefaultMethodResult
from datetime import datetime, timedelta
from sqlalchemy import and_, or_, update


class RequestDataAccess():
    dbSession = SessionManager().session    
    def AddRequest(self, name, description, status, createdby, updated) -> DefaultMethodResult:
        if updated.upper() == 'FALSE':
            isupdated = False
        else:
            isupdated = True
        createdat = datetime.now().isoformat()
        updatedat = createdat
        newrequest = Request(name = name, description = description, status = status, createdby = createdby, created_at = createdat, updated_at = updatedat, updated = isupdated)
        self.dbSession.add(newrequest)
        self.dbSession.commit()
        return DefaultMethodResult(True,'Request added')

    def GetRequests(self):
    #    request_schema = RequestSchema()
       request_schema = RequestSchema(many=True)
       requests = self.dbSession.query(Request).order_by(Request.requestid).all()
       return request_schema.dump(requests)
