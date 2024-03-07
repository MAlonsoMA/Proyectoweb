def importe_total_carro(request):
    total=0
    """session=request.session
    carro=session.get("carro")
    if not carro:
        carro=request.session["carro"]={}"""
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total=total+float(value["precio"])
            total=round(total,2)
        
    return {"importe_total_carro":total}