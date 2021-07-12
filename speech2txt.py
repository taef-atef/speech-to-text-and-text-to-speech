#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install ibm_watson


# In[2]:


pip install ibm_cloud_sdk_core


# In[1]:


from ibm_watson import TextToSpeechV1


# In[2]:


from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[3]:


api=IAMAuthenticator('oL2eTpIINazjXif2BR8p4oFNEJH3oN3E-bnPIawKoOEY')


# In[7]:


txt2speech=TextToSpeechV1(authenticator=api)
txt2speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/ad036d83-ffdc-439d-8651-89378f516445')


# In[8]:


with open("speech.mp3","wb") as audiofile:
    audiofile.write(
        txt2speech.synthesize("Hello, this is python and IBM homework it was really amazing coding with this features",accept="audio/mp3").get_result().content
    )


# In[ ]:





# In[ ]:





# In[ ]:




