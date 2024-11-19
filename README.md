# Algoritma

Ahmad Mujahid
F55123062

<h2>Merge Sort</h2>
    <ul>
        <li>
            <strong>Best Case:</strong> <code>O(n log n)</code><br>
            Berlaku untuk semua kasus karena proses penggabungan data selalu melibatkan pembagian array menjadi dua bagian secara terstruktur.
        </li>
        <li>
            <strong>Worst Case:</strong> <code>O(n log n)</code><br>
            Sama seperti best case, karena langkah-langkah pembagian dan penggabungan array dilakukan dengan metode yang konsisten.
        </li>
        <li>
            <strong>Average Case:</strong> <code>O(n log n)</code><br>
            Secara rata-rata, waktu yang dibutuhkan tetap <code>O(n log n)</code> karena algoritma bekerja dengan cara yang teratur di semua skenario.
        </li>
    </ul>

<h2>Quick Sort</h2>
    <ul>
        <li>
            <strong>Best Case:</strong> <code>O(n log n)</code><br>
            Terjadi saat pivot dapat membagi array secara merata menjadi dua bagian yang seimbang.
        </li>
        <li>
            <strong>Worst Case:</strong> <code>O(n<sup>2</sup>)</code><br>
            Terjadi jika pivot yang dipilih selalu menjadi elemen terkecil atau terbesar, sehingga pembagian array menjadi sangat tidak seimbang.
        </li>
        <li>
            <strong>Average Case:</strong> <code>O(n log n)</code><br>
            Rata-rata kasus memerlukan <code>O(n log n)</code>, karena biasanya pivot mampu membagi array dengan cukup seimbang, menghasilkan efisiensi yang baik.
        </li>
    </ul>
