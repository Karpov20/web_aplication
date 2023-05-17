"""
Задание 5.3a
Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'
Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

template = {
    'access_template': [
        "switchport mode access",
        "switchport access vlan {}",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    ],

    'trunk_template': [
        "switchport trunk encapsulation dot1q",
        "switchport mode trunk",
        "switchport trunk allowed vlan {}",
    ]
}

mode = input('Enter the interface operation mode (access/trunk): ')
interface = input('Enter the interface type and number: ')
question_template = {
    'access': 'Enter the number VLAN: ',
    'trunk': 'Enter allowed VLANS: '
}
temp_vlan = input(question_template[mode])
temp = mode + '_template'
print('\n' + '-' * 30)
print('interface {}'.format(interface))
print('\n'.join(template[temp]).format(temp_vlan))