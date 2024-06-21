#include<iostream>
#include<vector>
void BubbleSort(double* arr, int number);
using namespace std;
int main()
{
	int nums;
	cin >> nums;
	double* list = new double[nums]; //这行不会，回头要学习
	for (int i = 0; i < nums; i++)
	{
		cin >> list[i];
	}
	BubbleSort(list, nums);
	//输出排序后的数组
	for (int n = 0; n < nums; n++)
	{
		cout << list[n] << " ";
	}
	delete[] list;
	return 0;
}
void BubbleSort(double* arr, int number)
{
	double temp = 0;
	for (int i = 0; i < number; i++)
	{
		for (int j = 0; j < number - i - 1; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}