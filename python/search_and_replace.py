import os
from plushy.constants import TA, COMPANY



def convert_name( n ):
    nn = n.replace( "_ID", "" )
    return nn

def convert_company( n ):
    nn = n.replace( "_ID", "" )
    return nn

def clean_file( f ):
    ff = open( f, 'r' )
    change = 0
    for r in ff.readlines():
        if r.find( 'TA.' ) > -1:
            change = 1
        if r.find( 'COMPANY.' ) > -1:
            change = 1

    if change:

        print 'change'
        ff.seek(0)
        nf = open( f + ".new", 'w' )
        for r in ff.readlines():
            if r.find( 'TA.' ) > -1:
                for ta in TA.therapy_area_dict:
                    cname = convert_name( TA.id_to_name( ta, 'const_name' ) )
                    if r.find( cname ) > -1:
	                r =r .replace( cname, TA.id_to_name( ta, 'const_name' ) )
            if r.find( 'COMPANY.' ) > -1:
                for comp in COMPANY.company_dict:
                    cname = convert_company( COMPANY.id_to_name( comp, 'const_name' ) )
                    if r.find( cname ) > -1:
	                r =r .replace( cname, COMPANY.id_to_name( comp, 'const_name' ) )

            nf.write( r )

        nf.close()

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if name[-3:] == '.py':
            clean_file( os.path.join( root, name) ) 

