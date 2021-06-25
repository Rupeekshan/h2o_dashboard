from synth import FakeTimeSeries
from h2o_wave import main, app, Q, ui, site, data

page = site['/samp']

page['meta'] = ui.meta_card(box='', layouts=[
    ui.layout(
        # If the viewport width >= 0:
        breakpoint='xs',
        zones=[
            # 80px high header
            ui.zone('header', size='80px'),
            # Use remaining space for content
            ui.zone('content')
        ]
    ),
    ui.layout(
        # If the viewport width >= 768:
        breakpoint='m',
        zones=[
            # 80px high header
            ui.zone('header', size='80px'),
            # Use remaining space for body
            ui.zone('body', direction=ui.ZoneDirection.ROW, zones=[
                # 250px wide sidebar
                ui.zone('sidebar', size='250px'),
                # Use remaining space for content
                ui.zone('content'),
            ]),
            ui.zone('footer'),
        ]
    ),
    ui.layout(
        # If the viewport width >= 1200:
        breakpoint='l',
        # width='1500px',
        zones=[
            # 80px high header
            ui.zone('header', size='80px'),
            # Use remaining space for body
            ui.zone('first', direction=ui.ZoneDirection.ROW, zones=[
                ui.zone('r1c1', size='25%'),
                ui.zone('r1c2', size='25%'),
                ui.zone('r1c3', size='25%'),
                ui.zone('r1c4', size='25%'),
            ]),
            ui.zone('second', direction=ui.ZoneDirection.ROW, zones=[
                ui.zone('r2c1', size='50%'),
                ui.zone('r2c2', size='25%'),
                ui.zone('r2c3'),
            ]),
            ui.zone('third', direction=ui.ZoneDirection.ROW, zones=[
                ui.zone('r3c1', size='30%'),
                ui.zone('r3c2', size='30%'),
                ui.zone('r3c3'),
            ]),
            ui.zone('fourth', direction=ui.ZoneDirection.ROW, zones=[
                ui.zone('r4c1', size='50%'),
                ui.zone('r4c2'),
            ]),

            ui.zone('footer'),
        ]
    )
])

page['header'] = ui.header_card(
    # Place card in the header zone, regardless of viewport size.
    box='header',
    title='Dashboard',
    subtitle='Sample dashboard for testing',
    nav=[
        ui.nav_group('Menu', items=[
            ui.nav_item(name='#', label='Categories', icon='list'),
            ui.nav_item(name='#', label='Entries', icon='entry'),
            ui.nav_item(name='#', label='Assets', icon='gallery'),
        ]),
        ui.nav_group('User', items=[
            ui.nav_item(name='#', label='Profile', icon='user'),
            ui.nav_item(name='#', label='Settings', icon='settings'),
        ]),
        ui.nav_group('Help', items=[
            ui.nav_item(name='#', label='About', icon='info'),
            ui.nav_item(name='#', label='Support', icon='tools'),
        ])
    ],
)

flag = 'n'
row = 4
for i in range(1,row+1):
    if i == "2":
        ran = 4
    elif i == "4":
        ran = 3
    else:
        ran = 5

    for j in range(1,ran):
        
        page[f'row_{i}_{j}'] = ui.markdown_card(
            box=f'r{i}c{j}',
            title=f'ROW {i} - COLUMN {j}',
            content='Sample contents to test all layouts',
        )
    

page['footer'] = ui.markdown_card(
    box='footer',
    title='FOOTER',
    content='Sample contents to test all layouts',
)   

page.save()
