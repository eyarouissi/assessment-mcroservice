#from _typeshed import ReadableBuffer
from re import MULTILINE
import pydantic
from bson import ObjectId
import bson
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str
from fastapi import APIRouter, Body,  Request
from fastapi.encoders import jsonable_encoder
import pymongo
from starlette.routing import request_response 
from database.database import *
from models.assessment import *
from config import settings
from motor.motor_asyncio import AsyncIOMotorClient
import  pymongo
import asyncio
router = APIRouter()



#update assesments
@router.post("/assessments", response_description="update assesment in DB")
async def update_users(request: dict):
    user_data = jsonable_encoder(request)
    user_roles=[]
    nontailored_roles=[]
    assessments=user_data['assessments']

    if assessments == []  :
             return ErrorResponseModel("An error occured.", 404, " The assessments list must contain at least one assessment")
    else:
        
      for assessment in assessments:
        name=assessment['assessmentName']
        description=assessment['assessmentDescription']
        duration=assessment['assessmentDuration']
        provider=assessment['assessmentProvider']
        NumberOfQuestions=assessment["assessmentNumberOfQuestions"]
        type=assessment['assessmentType']
        if type=="internal":
           assessmentId = assessment["assessmentId"]
           assessmentLinkId=assessment["assessmentLinkId"]
           Assessments_collection.insert_one({ "_id": ObjectId(),"assessmentName":name,"assessmentDescription":description,"assessmentDuration":duration,"assessmentProvider":provider,"assessmentNumberOfQuestions":NumberOfQuestions,"assessmentType":type,"assessmentId":assessmentId,"assessmentLinkId":assessmentLinkId  })
        else:
            assessmentLink=assessment["assessmentLink"]
            Assessments_collection.insert_one({ "_id": ObjectId(),"assessmentName":name,"assessmentDescription":description,"assessmentDuration":duration,"assessmentProvider":provider,"assessmentNumberOfQuestions":NumberOfQuestions,"assessmentType":type,"assessmentLink":assessmentLink  })
          
      
      return ResponseModel_post("", "the assessments : {} are added successfully".format(request))

      
    
