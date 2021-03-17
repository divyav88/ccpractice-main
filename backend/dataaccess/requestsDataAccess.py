# dataaccess\requestDataAccess.py
from entities.request import Request, RequestSchema
from entities.databaseSessionManager import SessionManager
from models.defaultMethodResult import DefaultMethodResult
from datetime import datetime, timedelta
from sqlalchemy import and_, or_, update


class RequestDataAccess():
    dbSession = SessionManager().session    
    def AddRequest(self, name, description, status, createdby, updated) -> DefaultMethodResult:      
        createdat = datetime.now().isoformat()
        updatedat = createdat         
        newrequest = Request(name = name, description = description, status = status, createdby = createdby, created_at = createdat, updated_at = updatedat, updated = updated)
        self.dbSession.add(newrequest)
        self.dbSession.commit()
        return DefaultMethodResult(True,'Request added')
    def DeleteRequest(self, requestid) -> DefaultMethodResult:
        request = self.dbSession.query(Request).filter_by(requestid=requestid).first()         
        self.dbSession.delete(request)
        self.dbSession.commit()
        return DefaultMethodResult(True,'Request deleted')
    def EditRequest(self, requestid, name, description, status, createdby, updated) -> DefaultMethodResult:
        isupdated = updated
        # if updated.upper() == 'FALSE':
        #     isupdated = False
        # else:
        #     isupdated = True
        updatedat = datetime.now().isoformat()
        self.dbSession.query(Request).filter_by(requestid=requestid).update({Request.name:name, Request.description:description, Request.status:status, Request.createdby:createdby, Request.updated_at:updatedat, Request.updated:isupdated}, synchronize_session = False)
        self.dbSession.commit()
        return DefaultMethodResult(True,'Request updated')
    def GetRequests(self):
    #    request_schema = RequestSchema()
       request_schema = RequestSchema(many=True)
       requests = self.dbSession.query(Request).order_by(Request.requestid).all()
       return request_schema.dump(requests)