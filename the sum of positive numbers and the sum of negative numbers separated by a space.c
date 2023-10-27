#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    int values[N];
    int sum_positive = 0;
    int sum_negative = 0;

    for (int i = 0; i < N; i++) {
        scanf("%d", &values[i]);
        if (values[i] > 0) {
            sum_positive += values[i];
        } else if (values[i] < 0) {
            sum_negative += values[i];
        }
    }

    printf("%d %d\n", sum_positive, sum_negative);

    return 0;
}
