def checkParticipants(participants):
    return [k for k,v in enumerate(participants) if v<k ]