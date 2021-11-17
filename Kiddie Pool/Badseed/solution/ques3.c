main(){
	int v2 = time(0);
	srand(v2);
	int v9 = rand();
	srand(v9);
	int v10 = rand();
	int v12 = v9/v10%1000;
	printf("%d\n", v12);
}