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
            ui.zone('first', direction=ui.ZoneDirection.ROW, zones=[
                ui.zone('r1c1', size='25%'),
                ui.zone('r1c2', size='25%'),
                ui.zone('r1c3', size='25%'),
                ui.zone('r1c4', size='25%'),
                
                # ui.zone('other', zones=[
                #     # Use one half for charts
                #     ui.zone('charts', direction=ui.ZoneDirection.ROW),
                #     # Use other half for content
                #     ui.zone('content'),
                # ]),
            ]),
            ui.zone('second', direction=ui.ZoneDirection.ROW, zones=[
                ui.zone('r2c1', size='20%'),
                ui.zone('r2c2', size='60%'),
                ui.zone('r2c3'),
            ]),
            # # Use remaining space for body
            # ui.zone('body', direction=ui.ZoneDirection.ROW, zones=[
            #     # 300px wide sidebar
            #     # ui.zone('sidebar', size='300px'),
            #     # Use remaining space for other widgets
            #     ui.zone('content0', size='300px'),
            #     ui.zone('content1', size='300px'),
            #     ui.zone('content2', size='300px'),
            #     ui.zone('content3', size='300px'),
            #     ui.zone('content4', size='300px'),
            #     # ui.zone('other', zones=[
            #     #     # Use one half for charts
            #     #     ui.zone('charts', direction=ui.ZoneDirection.ROW),
            #     #     # Use other half for content
            #     #     ui.zone('content', size='250px'),
            #     # ]),
            # ]),
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

# for i in range(5):
#     page[f'bar_stat_{i}'] = ui.wide_bar_stat_card(
#         box=ui.boxes('content', 'sidebar', f'content{i}'),
#         title="Jingle bells",
#         value='=${{intl foo minimum_fraction_digits=2 maximum_fraction_digits=2}}',
#         aux_value='={{intl bar style="percent" minimum_fraction_digits=2 maximum_fraction_digits=2}}',
#         plot_color='$red',
#         progress=0.3,
#         data=dict(foo=10, bar=0.5),
#     )

for i in range(1,5):
    page[f'stat_{i}'] = ui.wide_bar_stat_card(
        box=ui.boxes('content', 'sidebar', f'r1c{i}'),
        title="Jingle bells",
        value='=${{intl foo minimum_fraction_digits=2 maximum_fraction_digits=2}}',
        aux_value='={{intl bar style="percent" minimum_fraction_digits=2 maximum_fraction_digits=2}}',
        plot_color='$red',
        progress=0.3,
        data=dict(foo=10, bar=0.5),
    )

for i in range(1,5):
    page[f'stat_{i}'] = ui.wide_bar_stat_card(
        box=ui.boxes('content', 'sidebar', f'r1c{i}'),
        title="Jingle bells",
        value='=${{intl foo minimum_fraction_digits=2 maximum_fraction_digits=2}}',
        aux_value='={{intl bar style="percent" minimum_fraction_digits=2 maximum_fraction_digits=2}}',
        plot_color='$red',
        progress=0.3,
        data=dict(foo=10, bar=0.5),
    )

for i in range(1,4):
    page[f'text_{i}'] = ui.markdown_card(
        box=ui.boxes('content', 'sidebar', f'r2c{i}'),
        title='Hello World',
        content='"The Internet? Is that thing still around?" - *Homer Simpson*',
    )

page.save()
