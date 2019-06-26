import requests
import json

def inbound(message):
  print('inbound v2')
  print(message.type)
  print(message.content)
  print(message.sender.id)
  print(message.sender.id.split('@')[0])
  print(message.sender.get_safe_name())
  print(message.timestamp)

  event = 'inbound'
  createdAt = 'now()'
  # messageType = 'message.type'
  # messageBody = 'message.content'
  # flow = 'from'
  # status = 'inbound'
  # fromNo = message.sender.id.split('@')[0]
  # toNo = '+60178567626'
  # leadName = message.sender.get_safe_name()
  # leadPhone = message.sender.id.split('@')[0]
  # leadImage = ''
  # lastSeen = ''
  # leadInfo = ''

  # createdAt = content['data']['date']
  messageType = 'message_type: "' + message.type + '",'
  messageBody = 'message_body: "' + (message.content or '') + '",'
  flow = 'flow: "' + 'inbound' + '",'
  status = 'status: "' + 'active' + '",'
  fromNo = 'from_no: "+' + message.sender.id.split('@')[0] + '",'
  toNo = 'to_number: "' + '+60178567626' + '",'

  leadName = 'name: "' + message.sender.get_safe_name() + '",'
  leadPhone = 'mobile_no: "' + message.sender.id.split('@')[0] + '",'

  leadInfo = '''
      lead: {
        data: {
          ''' + (leadName or '') + '''
          ''' + (leadPhone or '') + '''
        },
        on_conflict: {
          constraint: leads_mobile_no_key,
          update_columns: [name, image_url, last_seen]
        }
      }
  '''
  mutation = '''
  mutation {
    insert_inbound (objects: [{
      event: "''' + (event or '') + '''",
      created_at: "''' + (createdAt or '') + '''",
      ''' + (messageType or '') + '''
      ''' + (messageBody or '') + '''
      ''' + (flow or '') + '''
      ''' + (status or '') + '''
      ''' + (fromNo or '') + '''
      ''' + (toNo or '') + '''
      ''' + (leadInfo or '') + '''
    }]) {
      returning {
        id
      }
    }
  }
  '''
  print(mutation)
  url = 'https://hasura-whatsapi-premium.herokuapp.com/v1alpha1/graphql'
  jsonObj = { 'query' : mutation }
  headers = {
    'content-type': 'application/json',
    'x-hasura-admin-secret': '01200120'
  }

  r = requests.post(url=url, json=jsonObj, headers=headers)
  res = json.loads(r.text)
  print(res)
  return True
  # return request.form
