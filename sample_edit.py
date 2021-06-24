from h2o_wave import main, app, Q, ui, site

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
                # 300px wide sidebar
                ui.zone('sidebar', size='25%'),
                # Use remaining space for other widgets
                ui.zone('content', size='25%'),

                ui.zone('rest1', size='25%'),

                ui.zone('rest2', size='25%'),
                
                # ui.zone('other', zones=[
                #     # Use one half for charts
                #     ui.zone('charts', direction=ui.ZoneDirection.ROW),
                #     # Use other half for content
                #     ui.zone('content'),
                # ]),
            ]),
            ui.zone('second', direction=ui.ZoneDirection.ROW, zones=[
                
                ui.zone('col1', size='20%'),
                    # Use other half for content
                ui.zone('col2', size='60%'),

                ui.zone('col3'),
                
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
            ui.nav_item(name='#menu/spam', label='Spam'),
            ui.nav_item(name='#menu/ham', label='Ham'),
            ui.nav_item(name='#menu/eggs', label='Eggs'),
        ]),
        ui.nav_group('Help', items=[
            ui.nav_item(name='#about', label='About'),
            ui.nav_item(name='#support', label='Support'),
        ])
    ],
)

page['c1'] = ui.markdown_card(
    box='sidebar',
    title='COLUMN1',
    content='',
)
page['c2'] = ui.markdown_card(
    box='content',
    title='COLUMN2',
    content='',
)
page['c3'] = ui.markdown_card(
    box='rest1',
    title='COLUMN3',
    content='',
)
page['c4'] = ui.markdown_card(
    box='rest2',
    title='COLUMN4',
    content='',
)
page['c5'] = ui.markdown_card(
    box='row1',
    title='Second Row',
    content='',
)
page['c6'] = ui.markdown_card(
    box='col1',
    title='Second Row Col1',
    content='ddfsg',
)
page['c7'] = ui.markdown_card(
    box='col2',
    title='Second Row Col2',
    content='hrthr',
)
page['c8'] = ui.markdown_card(
    box='col3',
    title='Second Row Col2',
    content='hrthr',
)

page.save()
