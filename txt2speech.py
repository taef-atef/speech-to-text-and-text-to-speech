#!/usr/bin/env python
# coding: utf-8

# In[2]:


from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api='qpombChgxcJkXTbFEKh-ulPDGesRGQ2G_nTVOBSEYnz7'
url='https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/4f149214-b1dd-44b6-9174-6e60504ae6fc'

api=IAMAuthenticator(api)
s2t=SpeechToTextV1(authenticator=api)
s2t.set_service_url(url)


with open('speech.mp3','rb') as f:
    res=s2t.recognize(audio=f,content_type='audio/mp3',model='en-US_NarrowbandModel',continous=True).get_result()

text=res['results'][0]['alternatives'][0]['transcript']
with open('output.txt','w') as out:
    out.writelines(text)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




