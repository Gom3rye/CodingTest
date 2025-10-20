#include <iostream>
#include <vector>
#include <algorithm>

// C++의 빠른 입출력을 위한 설정
void setup_io() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
}

int main() {
    setup_io();

    int n, m;
    long long k; // 비용은 매우 커질 수 있으므로 long long 사용
    std::cin >> n >> m >> k;

    std::vector<int> oranges(n + 1);
    for (int i = 1; i <= n; ++i) {
        std::cin >> oranges[i];
    }

    // long long 타입의 매우 큰 값으로 초기화
    long long INF = 4e18; // 4 * 10^18, 충분히 큰 값
    std::vector<long long> dp(n + 1, INF);
    dp[0] = 0;

    // i는 0부터 n-1까지 순회 (Python의 range(n))
    for (int i = 0; i < n; ++i) {
        if (dp[i] == INF) {
            continue;
        }

        long long min_orange = 1e9 + 7; // int 최대값보다 크게
        long long max_orange = -1;

        // j는 상자의 크기 (1부터 m까지)
        for (int j = 1; j <= m; ++j) {
            int end_index = i + j;

            // 범위를 벗어나면 즉시 중단
            if (end_index > n) {
                break;
            }

            // 새 오렌지를 포함하여 min/max 갱신
            min_orange = std::min(min_orange, (long long)oranges[end_index]);
            max_orange = std::max(max_orange, (long long)oranges[end_index]);

            // 비용 계산
            long long box_cost = k + (long long)j * (max_orange - min_orange);

            // dp 테이블 갱신 (Push)
            dp[end_index] = std::min(dp[end_index], dp[i] + box_cost);
        }
    }

    std::cout << dp[n] << std::endl;

    return 0;
}