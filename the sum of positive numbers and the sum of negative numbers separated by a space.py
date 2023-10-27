#include <stdio.h>

int main() {
    int N;
    printf("Enter number of total number you want to enter: ");
    scanf("%d", &N);

    int values[N];
    int sum_positive = 0;
    int sum_negative = 0;
    
    printf("Enter your number in integer: ");
    
    for (int i = 0; i < N; i++) {
        scanf("%d", &values[i]);
            if (values[i] > 0) {
                sum_positive += values[i];
            } else if (values[i] < 0) {
                sum_negative += values[i];
        }
    }

    printf("The sum of positive number is: %d \nThe sum of negative number is: %d\n", sum_positive, sum_negative);

    return 0;
}
