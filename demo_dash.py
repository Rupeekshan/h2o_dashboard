from h2o_wave import main, app, Q, ui, site

page = site['/dash']

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
        breakpoint='xl',
        # width='1500px',
        zones=[
            # 80px high header
            ui.zone('header', size='80px'),
            # Use remaining space for body
            ui.zone('body', direction=ui.ZoneDirection.ROW, zones=[
                # 300px wide sidebar
                # ui.zone('sidebar', size='300px'),
                # Use remaining space for other widgets
                ui.zone('content0', size='300px'),
                ui.zone('content1', size='300px'),
                ui.zone('content2', size='300px'),
                ui.zone('content3', size='300px'),
                ui.zone('content4', size='300px'),
                # ui.zone('other', zones=[
                #     # Use one half for charts
                #     ui.zone('charts', direction=ui.ZoneDirection.ROW),
                #     # Use other half for content
                #     ui.zone('content', size='250px'),
                # ]),
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



page.save()
