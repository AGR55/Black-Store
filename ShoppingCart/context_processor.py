def total_money(request):
    total = 0

    if request.user.is_authenticated and 'shopping' in request.session:
        for key, value in request.session['shopping'].items():
            total += float(value['price'])

    return {'total_money': total}
