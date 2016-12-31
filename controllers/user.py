from gluon.storage import Storage


def login():
   import time
   form = FORM('Username',INPUT(_name='username', requires=[IS_NOT_EMPTY()]),
                'Password',INPUT(_name='password',_type='password' ,requires=[IS_NOT_EMPTY()]),
                INPUT(_type='submit',_value='Submit'))
   username = request.vars.username
   password = request.vars.password
   rows = db( (db.user.Username == username) & (db.user.Password==password)).select()
   if (form.process().accepted):
    # session.flash = "Wrong username or password"
     #redirect(URL('user','login'))
     if len(rows)==0:
         response.flash = "Wrong username or password"


     else:
         session.user = rows[0]
         return redirect(URL('default','index'))

   return dict(form=form,page_title="Login Screen")

def logout():
    global user
    user = None
    session.user = None
    return redirect(URL('default','index'))

def register():
       form = SQLFORM(db.user).process()
       return dict(form = form,page_title="Register");
def edit():
    return dict(page_title='Edit')
