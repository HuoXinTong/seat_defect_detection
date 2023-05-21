import os

def create_pos_n_impositive():
    for file_type in ['pos_train', 'impos_train']:
        for img in os.listdir(file_type):
            if (file_type == 'impos_train'):
                line = os.getcwd() + "\\" + file_type + '\\' + img + '\n'
                with open('impos.txt', 'a') as f:
                    f.write(line)
            elif (file_type == 'pos_train'):
                line = os.getcwd() + "\\" + file_type + '\\' + img + ' 1 0 0 20 20\n'
                with open('pos.txt', 'a') as f:
                    f.write(line)

if __name__ == '__main__':
    create_pos_n_impositive()
