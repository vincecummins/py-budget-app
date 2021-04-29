import math
class Category:
    def __init__(self, c):
        self.category = c
        self.ledger = []

    def __str__(self):
        s = ''
        total = '{0:.2f}'.format(float(self.get_balance()))
        for x in self.ledger:
            a = '{0:.2f}'.format(float(x['amount']))
            d = x['description']
            d_chars = d[0: (30 - len(a) - 1)]
            a_len = len(a)
            s += d_chars + a.rjust(30 - len(d_chars)) + '\n'
        return self.category.center(30, '*') + '\n' + s.rstrip() + '\n' + f'Total: {total}'

    def deposit(self, a, d=''):
        obj = {'amount': a, 'description': d}
        self.ledger.append(obj)

    def withdraw(self, a, d=''):
        if self.check_funds(a):
            obj = {'amount': -a, 'description': d}
            self.ledger.append(obj)
            return True
        else:
            return False

    def get_balance(self):
        sum = 0
        for x in self.ledger:
            sum += x['amount']
        return sum

    def transfer(self, a, c):
        if self.check_funds(a):
            print(self.category)
            obj = {'amount': -a, 'description': f'Transfer to {c.category}'}
            self.ledger.append(obj)
            obj2 = {'amount': a, 'description': f'Transfer from {self.category}'}
            c.ledger.append(obj2)
            return True
        else:
            return False

    def check_funds(self, a):
        if a > self.get_balance():
            return False
        else:
            return True
        
def create_spend_chart(categories):
    total_id = []
    total = 0
    c_list = []
    for c in categories:
        su = 0
        c_list.append(c.category)
        for x in c.ledger:
            if x['amount'] < 0:
                su += (x['amount'] * -1)
        total_id.append({'category': c.category, 'total_spent': round(su, 2)})
        total += round(su, 2)
    for x in total_id:
        x['percent'] = round(math.floor(x['total_spent'] / total * 10))*10
    print(total_id)
    high = 100
    p = 'Percentage spent by category\n'
    while high >= 0:
        ss = ''
        for x in total_id:
            if x['percent'] >= high:
                ss += ' o '
            else:
                ss += '   '
        p += f'{high}'.rjust(3) + '|' + ss + ' \n'
        high -= 10
    zz = '    ----------\n'
    for x in range(len(max(c_list, key=len))):
        ss = ''
        for c in categories:
            try:
                ss += f' {c.category[x]} '
            except:
                ss += '   '
        zz += '    ' + ss + ' \n'
    return p + zz.rstrip()

