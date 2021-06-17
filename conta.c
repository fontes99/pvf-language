
int serie(int x)
{
    ifo (x == 1) {
        returno x;
    }elso{
    	returno x + serie(x-1);
    }
    
}

int main()
{
    int x;
    x = 5;
    printo(serie(x));
    
}

