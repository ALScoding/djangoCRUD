from django.db import IntegrityError, transaction

@transaction.atomic
def viewfunc(request):
    create_parent()

    try:
        with transaction.atomic():
            generate_relationships()
    except IntegrityError:
        handle_exception()

    a.save() # Succeeds, but may be undone by transaction rollback
    try:
        b.save() # Could throw exception
    except IntegrityError:
        transaction.rollback()
    c.save() # Succeeds, but a.save() may have been undone