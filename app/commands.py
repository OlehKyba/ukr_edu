import click
from flask.cli import with_appcontext

from .extentions import db
from .models import User, Role, Post, Tag

from datetime import datetime


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()


@click.command(name='drop_db')
@with_appcontext
def drop_tables():
    db.drop_all()


@click.command(name='create_test_db')
@with_appcontext
def create_test_db():
    admin = User(
        name='admin',
    )

    admin.set_password('admin')

    student = User(
        name='oleh',
    )

    student.set_password('12345')

    users = [admin, student]

    admin_role = Role(name='admin')
    student_role = Role(name='student')

    admin.roles.append(admin_role)
    student.roles.append(student_role)

    roles = [admin_role, student_role]

    text = '''
                  <p>Barbeled houndshark koi gopher rockfish: Blacksmelt 
                  crevice kelpfish flyingfish Atlantic
                  trout--Colorado squawfish waryfish sleeper chain pickerel 
                  barracudina Bitterling ziege
                  airbreathing catfish. Bigmouth buffalo sole red velvetfish 
                  sixgill ray southern sandfish?
              </p>
              <p>Candiru loosejaw, Atlantic eel devil ray cowfish skipjack
               tuna Devario, spinefoot barreleye.
                  Razorfish neon tetra bonefish bigscale; threespine
                   stickleback cutlassfish false moray
                  common tunny duckbill long-whiskered catfish.</p>
              <p>Brown trout Atlantic eel pricklefish common carp; bocaccio
               powen convict cichlid. Convict
                  blenny lake whitefish mola mola sunfish yellow-eye mullet.
                   Driftwood catfish aholehole,
                  largenose fish false moray New Zealand sand diver,
                   Rabbitfish, barreleye longnose lancetfish
                  longfin smelt bowfin. Bonytail chub zingel dorab cownose 
                  ray threadsail lizardfish
                  mahi-mahi, bighead carp sailbearer wobbegong cuckoo wrasse,
                   sea bream peladillo ilisha
                  surfperch. Daggertooth pike conger pigfish bangus Redfin
                   perch ling antenna codlet, torrent
                  fish livebearer longfin escolar collared carpetshark?</p>
              <div class="embed-responsive embed-responsive-16by9">
                  <iframe class="embed-responsive-item" 
                  src="https://www.youtube.com/embed/jatrKiErgqA?rel=0"
                      allowfullscreen></iframe>
              </div>
              <p>Rough sculpin blue eye dragon goby channel catfish Owens 
              pupfish, gulper false moray Oregon
                  chub. Plownose chimaera madtom lighthousefish Bengal danio: 
                  yellow-edged moray; mummichog
                  skipping goby unicorn fish sculpin. Mrigal moray eel 
                  burrowing goby hairtail sawfish sculpin
                  kokopu hamlet combtooth blenny lightfish featherback 
                  Rainbowfish tripod fish loosejaw.
                  Glassfish angler catfish sand stargazer Mexican golden trout 
                  peamouth Black swallower
                  sleeper cardinalfish salamanderfish electric knifefish. Pike 
                  conger sleeper devil ray.</p>
              <p>Bream; orange roughy, central mudminnow Steve fish Billfish 
              ridgehead Alaska blackfish loach
                  goby icefish sea chub thresher shark, slickhead, wallago 
                  glassfish Bengal danio. Paperbone
                  driftwood catfish, northern pike tubeblenny electric eel, 
                  "electric ray kahawai striped
                  burrfish grideye cowfish zebra trout betta longjaw mudsucker
                   pike characid, mola mola
                  sunfish." Sábalo sarcastic fringehead kahawai surgeonfish
                   pelagic cod Mexican blind cavefish
                  muskellunge pencilsmelt wolffish viperfish glass catfish 
                  stream catfish! Sand diver
                  elephantnose fish coho salmon slimy sculpin striped burrfish; 
                  lake chub giant wels?</p>
                   '''

    post1 = Post(
        title='Енеїда',
        subtitle='''«Енеїда» — українська бурлескно-травестійна
                    поема, написана письменником Іваном 
                    Котляревським, на сюжет однойменної 
                    класичної поеми римського поета Вергілія.''',
        text=text,
        date=datetime(2019, 1, 1, 12, 30, 59, 0)
    )

    post1.author = admin

    post2 = Post(
        title='День прапору',
        subtitle='''«Енеїда» — українська бурлескно-травестійна
                    поема, написана письменником Іваном 
                    Котляревським, на сюжет однойменної 
                    класичної поеми римського поета Вергілія.''',
        text=text,
        date=datetime(2015, 1, 1, 12, 30, 59, 0)
    )

    post2.author = admin

    post3 = Post(
        title='Ми відкрились!',
        subtitle='''«Енеїда» — українська бурлескно-травестійна
                    поема, написана письменником Іваном 
                    Котляревським, на сюжет однойменної 
                    класичної поеми римського поета Вергілія.''',
        text=text,
        date=datetime(2016, 1, 1, 12, 30, 59, 0)
    )

    post3.author = admin

    posts = [post1, post2, post3]

    tag1 = Tag(value='Україна')
    tag2 = Tag(value='укр літр')
    tag3 = Tag(value='сайт')

    tag1.posts.append(post1)
    tag1.posts.append(post2)
    tag1.posts.append(post3)

    tag2.posts.append(post1)
    tag2.posts.append(post2)

    tag3.posts.append(post3)

    tags = [tag1, tag2, tag3]

    db.session.add_all(users)
    db.session.add_all(roles)
    db.session.add_all(posts)
    db.session.add_all(tags)

    db.session.commit()
