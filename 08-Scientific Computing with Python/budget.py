
class Category:

    def __init__(self, category) -> None:
        self.category= category
        self.ledger = []
        pass
    def deposit(self, amount, description=''):
        self.ledger.append( {'amount':amount, 'description':description} )
        pass
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) is False:
            return False
        self.ledger.append( {'amount':-amount, 'description':description} )
        return True
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance;
    def transfer(self, amount, transferTo):
        if self.check_funds(amount) is False:
            return False
        self.withdraw(amount, 'Transfer to ' + transferTo.category)
        transferTo.deposit(amount, 'Transfer from ' + self.category)
        return True
    def check_funds(self, amount):
        return False if amount > self.get_balance() else True
        
    def get_totalWithdraw(self):
        total = 0
        for item in filter( lambda x : x['amount']<0, self.ledger):
            total += item['amount']
        return abs(total)

    def print_budget(self):
        print('{:*^30}'.format(self.category))
        for item in self.ledger:
            print('{:<23}{:>7.2f}'.format(item['description'], item['amount']))
        print('Total: {:.2f}'.format(self.get_balance()))
        pass

def create_spend_chart(categorys):
    # >> ***** pplot-class *****
    class pplot:
        @staticmethod
        def move(x,y):
            if x != 0:
                lr = 'D' if x < 0 else 'C' # left - ..o.. + Right
                print( '\033[{}{}'.format(abs(x), lr), end='')
            if y != 0:
                tb = 'A' if y > 0 else 'B' # Top  + ..o.. - Bottom
                print( '\033[{}{}'.format(abs(y), tb), end='')
        @staticmethod
        def plotname(x,y,name): # x,y: offset from printorg
            pplot.move(x,y)
            for i, c in enumerate(name):
                print(c, end='')
                pplot.move(-1,-1)
            pplot.move(-x,len(name)-y)
        @staticmethod
        def plotchart(x,y_zero, o_count): # x,y: offset from printorg
            pplot.move(x,y_zero)
            for i in range(o_count):
                print('o', end='')
                pplot.move(-1,1)
            pplot.move(-x,-o_count-y_zero)
    # << ***** pplot-class *****

    # initialize parameter 
    maxlen_category = 0
    for category in categorys:
        maxlen_category = max(maxlen_category, len(category.category))
    plot_w, plot_h = len(categorys) * 3 + 1, 11
    graph_w = 3 + 1 + plot_w
    
    form = lambda c, n : '{:' + str(c) + '^'+str(n)+'}'
    
    # print graph title
    print('Percentage spent by category')
    # fill graph area
    for i in range(plot_h):
        print(('{:>3}|' + form(' ',plot_w) ).format(100-i*10,''))
    print('    '+ form('-',plot_w).format(''))
    for i in range(maxlen_category):
        print(form(' ',graph_w).format('') )
        
    # plot category-name and chart    
    print_offset_x = 3
    print_offset_y = maxlen_category
    pplot.move(print_offset_x + 2, print_offset_y)
    
    for i, category in enumerate(categorys):
        pplot.plotname(i * 3, 0, category.category )
        percent_count = int(category.get_totalWithdraw() / 1000 * 100 + 5) // 10
        pplot.plotchart(i * 3, 2, min( 11, percent_count + 1))
        print_offset_x += 3
        
    pplot.move(-print_offset_x, -print_offset_y)

    # for i, category in enumerate(categorys):
    #     print(category.get_totalWithdraw(), ',' ,\
    #           int(category.get_totalWithdraw() / 1000 * 100 + 5) // 10)
    




if __name__=='__main__':
    clothing = Category('Clothing')
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more foo')
    food.transfer(50, clothing)

    total_withdraw = 0
    for item in filter( lambda x : x['amount']<0,  food.ledger):
        total_withdraw += item['amount']

    food.print_budget()
    print('')
    clothing.print_budget()
    print('')

    create_spend_chart([food])


