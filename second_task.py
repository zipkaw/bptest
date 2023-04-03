
def magic(w: int, 
          d: int, 
          P: int, 
          N: int) -> int:
    if w < d: 
        print('d - не может быть тяжелее w по условию')
        return 0
    result = int((w*N*(N-1)/2 - P)/d)
    if result > N:
        print('не верно задан вес взятых монет')
        return 0
    return 

w, d, P, N = list(map(int, input('Введите w, d, P, N, через запятую:').split(',')))

fake_n = magic(w, d, P, N)
if fake_n != 0: 
    print(f'Фальшивые монеты в {fake_n} корзине')
