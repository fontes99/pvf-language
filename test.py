import subprocess
import pytest
'''
To fix:

return de op booleanas esta byte, precisa retornar bool
'''

# test geral
def test_geral():
    with open('example.pvf', 'w') as f:
        f.write('''{
    int x;
    int y;
    int z; 
    x /*asdasda*/ = 3;
    y = 4;
    z = x + y + 100;
    printo(x + y /*asdasda*/ + z); 
}''')
    assert int(subprocess.check_output("python3 main.py example.pvf", shell=True)) == 114


def test_soma_simples():
    with open('example.pvf', 'w') as f:
        f.write('''{
    int x;
    x = 3;
    printo(x); 
}''')
    assert int(subprocess.check_output("python3 main.py example.pvf", shell=True)) == 3


def test_soma_varias():
    with open('example.pvf', 'w') as f:
        f.write('''{
    int x;
    int y;
    int z;

    x = 3;
    y = 5;
    z = 3 + 5;
    printo(z); 
}''')
    assert int(subprocess.check_output("python3 main.py example.pvf", shell=True)) == 8


def teste_issue():
    with open('example.pvf', 'w') as f:
        f.write('''{

    int x1;
    int y2;
    int z_final;

    x1 = 8;
    y2 = 5;



    z_final = (x1 + y2) * ---37;;
    printo(z_final); 
}''')
    assert int(subprocess.check_output("python3 main.py example.pvf", shell=True)) == -481


def teste_input_igual_2():
    with open('example.pvf', 'w') as f:
        f.write('''{

    int x_1;
    int y;
    int z_final_;

    x_1 = 8;
    y = 57;



    z_final_ = (x_1 + y) * readln();;
    printo(z_final_); 
}''')
    assert int(subprocess.check_output("python3 main.py example.pvf < input.txt", shell=True)) == 130


def teste_eq():
    with open('example.pvf', 'w') as f:
        f.write('''{

    int x;
    int y;
    bool z;

    x = 8;
    y = 57;



    z = x == y;;;
    printo(z); 
}''')
    assert subprocess.check_output("python3 main.py example.pvf", shell=True) == b'False\n'


def teste_block():
    with open('example.pvf', 'w') as f:
        f.write('''{

        int x; 
        int y;
        int z;

        {
            x = 8;
            y = 57;
        }

    z = x * y;;;
    printo(z); 
}''')
    assert int(subprocess.check_output("python3 main.py example.pvf", shell=True)) == 456

def teste_ifo():
    with open('example.pvf', 'w') as f:
        f.write('''{
    int x;
    int y;

    x = 3;
    y = 6;

    ifo (x+y < 10) 
        printo(1); 
    printo(0);
}''')
    assert int(subprocess.check_output("python3 main.py example.pvf", shell=True)) == 1

def teste_ifo_elso():
    with open('example.pvf', 'w') as f:
        f.write('''{
    int x;
    int y;

    x = 3;
    y = 7;

    ifo (x+y < 10) {
        printo(1); 
    } elso {
        printo(0);
    }
}''')
    assert int(subprocess.check_output("python3 main.py example.pvf", shell=True)) == 0

def teste_ifo_alone():
    with open('example.pvf', 'w') as f:
        f.write('''{

    int x;
    int y;

    x = 3;
    y = 7;

    ifo (x+y < 10) {
        printo(1); 
    } 

    printo(0);

}''')
    assert int(subprocess.check_output("python3 main.py example.pvf", shell=True)) == 0

def teste_ifo_elsoifo():
    with open('example.pvf', 'w') as f:
        f.write('''{

    int x;
    int y;

    x = 3;
    y = 7;

    ifo (x+y < 10) {
        printo(1); 
    } elso ifo (x == 3) {
        printo(0);
    }
}''')
    assert int(subprocess.check_output("python3 main.py example.pvf", shell=True)) == 0

def teste_ifo_elsoifo_elso():
    with open('example.pvf', 'w') as f:
        f.write('''{

    int x;
    int y;

    x = 3;
    y = 7;

    ifo (x+y < 10) {
        printo(0); 
    } elso ifo (x == 2) {
        printo(1);
    } elso {
        printo(2);
    }

}''')
    assert int(subprocess.check_output("python3 main.py example.pvf", shell=True)) == 2

def teste_whilo():
    with open('example.pvf', 'w') as f:
        f.write('''{
    int x;
    x = 0;

    whilo (x < 10) {
        x = x + 1;
    }

    printo(x);

}''')
    assert int(subprocess.check_output("python3 main.py example.pvf", shell=True)) == 10

def teste_string():
    with open('example.pvf', 'w') as f:
        f.write('''{
    string x;
    x = "oi";
    printo(x);
}''')
    assert subprocess.check_output("python3 main.py example.pvf", shell=True) == b'"oi"\n'

def teste_string():
    with open('example.pvf', 'w') as f:
        f.write('''{
    bool x;
    x = 1 > 0;
    printo(x);
}''')
    assert subprocess.check_output("python3 main.py example.pvf", shell=True) == b'True\n'

    