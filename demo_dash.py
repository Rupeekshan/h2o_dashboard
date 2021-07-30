from random import random
import time
from faker import Faker
from synth import FakeCategoricalSeries, FakeTimeSeries, FakeMultiTimeSeries, FakePercent, FakeMultiCategoricalSeries
from h2o_wave import main, app, Q, ui, site, data
from random import randint


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
                ui.zone('r2c3', size='25%'),
            ]),
            ui.zone('third', direction=ui.ZoneDirection.ROW, zones=[
                ui.zone('r3c1', size='40%'),
                ui.zone('r3c2', size='40%'),
                ui.zone('r3c3'),
            ]),
            ui.zone('fourth', direction=ui.ZoneDirection.ROW, zones=[
                ui.zone('r4c1', size='50%'),
                ui.zone('r4c2'),
            ]),
            ui.zone('fifth', direction=ui.ZoneDirection.ROW, zones=[
                ui.zone('r5c1', size='35%'),
                ui.zone('r5c2', size='35%'),
                ui.zone('r5c3'),
            ]),

            ui.zone('footer'),
        ]
    )
])

page['header'] = ui.header_card(
    # Place card in the header zone, regardless of viewport size.
    box='header',
    title='XYZ Apperals',
    subtitle='Production View ',
    nav=[
        ui.nav_group('Menu', items=[
            ui.nav_item(name='#', label='Employees Details', icon='list'),
            ui.nav_item(name='#', label='Production Details', icon='entry'),
            ui.nav_item(name='#', label='Products', icon='gallery'),
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

colors = '$red $pink $blue $azure $cyan $teal $mint $green $lime $yellow $amber $orange $tangerine'.split()
fake = Faker()
fc = FakeCategoricalSeries()
cat_g, val_g, pc_g = fc.next()
d = []

# <<<<<<<<--------------------FIRST ROW------------------------>>>>>>>>>>
details = ['', 'Total Employees', 'Absent Percentage',
           'Forecast Efficiency', 'Current Efficiency']
for i in range(1, 5):
    # if i == 3 or i == 4:
        # temp = {intl qux minimum_fraction_digits=0 maximum_fraction_digits=0}
    d.append(page.add(f'stat_{i}', ui.wide_series_stat_card(  # Employees Total
        box=ui.boxes('content', 'sidebar', f'r1c{i}'),
        title=details[i],  # fake.cryptocurrency_name(),
        value='={{intl qux minimum_fraction_digits=2 maximum_fraction_digits=2}}', # if i != 1 else '={{intl qux minimum_fraction_digits=0 maximum_fraction_digits=0}}'
        aux_value='={{intl quux style="percent" minimum_fraction_digits=1 maximum_fraction_digits=1}}',
        data=dict(qux=val_g, quux=pc_g / 100),
        plot_category='foo',
        plot_type='interval',
        plot_value='qux',
        plot_color=colors[randint(0, 12)],
        plot_data=data('foo qux', -15),
        plot_zero_value=0,
    )))


# <<<<<<<<--------------------SECOND ROW------------------------>>>>>>>>>>
n = 100  # Pcs with time
fm = FakeMultiTimeSeries()
g = page.add('graph', ui.plot_card(
    box='r2c1',
    title='PCs with time',
    data=data('product date price', n * 5),
    plot=ui.plot([ui.mark(type='area', x_scale='time', x='=date',
                          y='=price', color='=product', y_min=0)])
))

fp = FakePercent()

c = []
details_pcs = ['', 'Total PCs', 'Total PCs for the week']
for i in range(1, 3):
    val_c, pc_c = fp.next()
    c.append(page.add(f'gauge_{i}', ui.tall_gauge_stat_card(
        box=f'r2c{i+1}',
        title=details_pcs[i],  # Details_Pcs[i],  # fake.cryptocurrency_name(),
        value='={{intl foo minimum_fraction_digits=2 maximum_fraction_digits=2}}',
        aux_value='={{intl bar style="percent" minimum_fraction_digits=2 maximum_fraction_digits=2}}',
        plot_color=colors[i*4],
        progress=pc_c,
        data=dict(foo=val_c, bar=pc_c),
    )))


# <<<<<<<<--------------------THIRD ROW------------------------>>>>>>>>>>
ls = []
details_damage = ['', 'Damage Percentage', 'Pending Boxes', 'Delivered Boxes']
for i in range(1, 4):
    val_ls, pc_ls = fp.next()
    ls.append(page.add(f'l_stat_{i}', ui.large_stat_card(
        box=f'r3c{i}',
        title=details_damage[i],  # fake.cryptocurrency_name(),
        value='={{intl qux minimum_fraction_digits=2 maximum_fraction_digits=2}}',
        aux_value='={{intl quux style="percent" minimum_fraction_digits=1 maximum_fraction_digits=1}}',
        data=dict(qux=val_ls, quux=pc_ls),
        caption=' '.join(fake.sentences()),
    )))


# <<<<<<<<--------------------FOURTH ROW------------------------>>>>>>>>>>
table_fields = ['Date', 'Fabric Id', 'Total Count', 'CHN', 'BAN', 'IND', 'AFG']
table_rows = [
    ['2021-06-28', 'abc001', '118', '132', '129', '121', '121'],
    ['2021-06-27', 'abc001', '126', '141', '135', '125', '121'],
    ['2021-06-26', 'abc001', '150', '178', '163', '172', '121'],
    ['2021-06-25', 'abc001', '180', '193', '181', '183', '121'],
    ['2021-06-24', 'abc001', '196', '236', '235', '229', '121'],
    ['2021-06-23', 'abc001', '188', '235', '227', '234', '121'],
]


# Methods used for table 
def make_markdown_row(values):
    return f"| {' | '.join([str(x) for x in values])} |"


def make_markdown_table(fields, rows):
    return '\n'.join([
        make_markdown_row(fields),
        make_markdown_row('---' * len(fields)),
        '\n'.join([make_markdown_row(row) for row in rows]),
    ])


page.add('table', ui.form_card(
    box='r4c1',
    items=[
        ui.text(make_markdown_table(
            fields=table_fields,
            rows=table_rows,
        )),
    ],
))


np = 10
k = 5
fmc = FakeMultiCategoricalSeries(groups=k)

p = page.add('plot', ui.plot_card(
    box='r4c2',
    title='Last Month Success Rate',
    data=data('country product price', np * k),
    plot=ui.plot([ui.mark(type='interval', x='=price',
                          y='=product', color='=country', stack='auto', y_min=0)])
))


# <<<<<<<<--------------------FIFTH ROW------------------------>>>>>>>>>>
curves = 'smooth step linear'.split()
cards = []
sw = []
details_machine = ['', 'Available Sewing Machine',
                   'Available Cutting Quantity', 'Total Style Changes next week']
for i in range(1, 4):
    cat_sw, val_sw, pc_sw = fc.next()
    w = page.add(f'stat_wide_{i}', ui.wide_series_stat_card(
        box=f'r5c{i}',
        title=details_machine[i],  # fake.cryptocurrency_name(),
        value='={{intl qux minimum_fraction_digits=2 maximum_fraction_digits=2}}',
        aux_value='={{intl quux style="percent" minimum_fraction_digits=1 maximum_fraction_digits=1}}',
        data=dict(qux=val_sw, quux=pc_sw / 100),
        plot_category='foo',
        plot_type='area',
        plot_value='qux',
        plot_color=colors[i],
        plot_data=data('foo qux', -15),
        plot_zero_value=0,
        plot_curve=curves[i-1],
    ))
    cards.append((fc, w))

page.save()

# <<<<<<<<--------------------UPDATE------------------------>>>>>>>>>>
while True:
    time.sleep(0.5)

    for card in d:
        cat_g, val_g, pc_g = fc.next()
        card.data.qux = val_g
        card.data.quux = pc_g / 100
        card.plot_data[-1] = [cat_g, val_g]

    g.data = [(g, t, x) for x in [fm.next() for _ in range(n)]
              for g, t, x, dx in x]

    p.data = [(g, t, x) for x in [fmc.next() for _ in range(np)]
              for g, t, x, dx in x]

    for i in range(1, 3):
        val_c, pc_c = fp.next()
        c[i-1].data.foo = val_c
        c[i-1].data.bar = pc_c
        c[i-1].progress = pc_c

    for i in range(1, 4):
        val_ls, pc_ls = fp.next()
        ls[i-1].data.qux = val_ls
        ls[i-1].data.quux = pc_ls

    for f, b in cards:
        cat_sw, val_sw, pc_sw = f.next()
        b.data.qux = val_sw
        b.data.quux = pc_sw / 100
        b.plot_data[-1] = [cat_sw, val_sw]

    page.save()
