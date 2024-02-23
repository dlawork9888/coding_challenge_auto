# [level 1] 여러 기준으로 정렬하기 - 59404 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/59404) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > SELECT

### 채점결과

ANIMAL_IDNAMEDATETIMEA3689302014-06-08 13:20:00A362383*Morado2016-04-21 08:19:00A412626*Sam2016-03-13 11:17:00A403564Anna2013-11-18 17:03:00A371534April2016-06-07 17:42:00A354597Ariel2014-05-02 12:16:00A361391Baby Bear2015-03-30 11:36:00A413789Benji2016-04-19 13:28:00A353259Bj2016-05-08 12:57:00A388691Blaze2015-11-27 15:59:00A371102Ceballo2015-08-03 09:09:00A397882Charlie2017-07-12 14:43:00A381217Cherokee2017-07-08 09:41:00A410330Chewy2016-09-11 14:09:00A392615Chip2015-07-26 11:39:00A385442Clyde2014-01-11 15:15:00A367438Cookie2015-09-10 16:01:00A387965Dakota2014-06-25 16:58:00A375393Dash2015-06-12 12:47:00A365172Diablo2014-08-26 12:53:00A379998Disciple2013-10-23 11:42:00A376459Dora2017-07-09 07:42:00A355753Elijah2015-09-10 13:14:00A373219Ella2014-07-29 11:43:00A370507Emily2014-10-27 14:43:00A355519Faith2015-05-08 18:34:00A383964Finney2017-02-05 12:27:00A378348Frijolito2014-01-25 14:38:00A358697Fuzzo2015-02-06 12:12:00A352713Gia2017-04-13 16:29:00A386005Giovanni2015-09-25 18:17:00A362707Girly Girl2016-01-27 12:27:00A387083Goldie2014-02-01 18:36:00A363653Goofy2014-11-17 17:39:00A371000Greg2015-07-29 16:07:00A357846Happy2016-03-17 14:09:00A352555Harley2014-08-08 04:20:00A390222Holly2013-12-08 17:04:00A362967Honey2014-06-08 18:19:00A364429Hugo2015-09-28 16:26:00A399552Jack2013-10-14 15:38:00A412697Jackie2016-01-03 16:25:00A407156Jake2016-10-18 11:01:00A384568Jedi2014-12-13 15:19:00A350276Jewel2017-08-13 13:50:00A412173Jimminee2015-07-28 18:17:00A384360Jj2014-07-04 01:55:00A405494Kaila2014-05-16 14:17:00A370852Katie2013-11-03 15:04:00A354725Kia2015-08-26 11:51:00A380420Laika2017-08-04 16:45:00A408035Lizzie2014-12-25 12:02:00A377750Lucy2017-10-25 17:17:00A400680Lucy2017-06-17 13:29:00A399421Lucy2015-08-25 14:08:00A378353Lyla2014-08-02 11:23:00A376322Mama Dog2014-02-18 12:24:00A382192Maxwell 22015-03-13 13:14:00A350375Meo2017-03-06 15:01:00A378946Mercedes2017-09-28 13:36:00A367012Miller2015-09-16 09:06:00A365302Minnie2017-01-08 16:34:00A410684Mitty2014-06-21 12:25:00A391858Nellie2017-03-16 16:53:00A383036Oreo2014-05-29 12:31:00A352872Peanutbutter2015-07-09 17:51:00A392027Penny2014-01-31 13:46:00A381173Pepper2014-08-06 12:07:00A380009Pickle2016-02-01 14:35:00A382251Princess2014-11-08 16:14:00A386688Punch2015-08-17 12:55:00A357444Puppy2016-03-11 15:43:00A357021Queens2014-12-03 15:15:00A396810Raven2016-08-22 16:13:00A410668Raven2015-11-19 13:41:00A400498Reggie2016-10-04 20:31:00A414513Rocky2016-06-07 09:17:00A395451Rogan2015-12-27 17:42:00A391512Rome2016-04-06 15:53:00A373687Rosie2014-03-20 12:31:00A380506Ruby2016-01-22 17:13:00A406756Sabrina2016-05-12 20:23:00A371344Sailor2015-05-11 12:33:00A354753Sammy2017-04-21 11:33:00A380320Scooby2014-02-03 12:41:00A355688Shadow2014-01-26 13:48:00A414198Shelly2015-01-29 15:01:00A358879Simba2015-09-14 16:52:00A392075Skips2013-11-20 13:09:00A394547Snickerdoodl2015-01-24 16:14:00A370439Sniket2016-06-25 11:46:00A388360Spider2015-12-25 10:13:00A409637Stanley2016-04-02 11:36:00A362103Stitch2014-11-18 21:20:00A368742Stormy2018-02-03 10:40:00A349996Sugar2018-01-22 14:32:00A386276Tiko2015-12-19 12:52:00A354540Tux2014-12-11 11:48:00A367747Woody2014-10-19 14:49:00A378818Zoe2014-07-05 07:13:00

### 제출 일자

2024년 02월 23일 19:38:28

### 문제 설명

<p><code>ANIMAL_INS</code> 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. <code>ANIMAL_INS</code> 테이블 구조는 다음과 같으며, <code>ANIMAL_ID</code>, <code>ANIMAL_TYPE</code>, <code>DATETIME</code>, <code>INTAKE_CONDITION</code>, <code>NAME</code>, <code>SEX_UPON_INTAKE</code>는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>NAME</th>
<th>TYPE</th>
<th>NULLABLE</th>
</tr>
</thead>
        <tbody><tr>
<td>ANIMAL_ID</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>ANIMAL_TYPE</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>DATETIME</td>
<td>DATETIME</td>
<td>FALSE</td>
</tr>
<tr>
<td>INTAKE_CONDITION</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>NAME</td>
<td>VARCHAR(N)</td>
<td>TRUE</td>
</tr>
<tr>
<td>SEX_UPON_INTAKE</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p>동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해주세요. 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.</p>

<h5>예시</h5>

<p>예를 들어, <code>ANIMAL_INS</code> 테이블이 다음과 같다면</p>
<table class="table">
        <thead><tr>
<th>ANIMAL_ID</th>
<th>ANIMAL_TYPE</th>
<th>DATETIME</th>
<th>INTAKE_CONDITION</th>
<th>NAME</th>
<th>SEX_UPON_INTAKE</th>
</tr>
</thead>
        <tbody><tr>
<td>A349996</td>
<td>Cat</td>
<td>2018-01-22 14:32:00</td>
<td>Normal</td>
<td>Sugar</td>
<td>Neutered Male</td>
</tr>
<tr>
<td>A350276</td>
<td>Cat</td>
<td>2017-08-13 13:50:00</td>
<td>Normal</td>
<td>Jewel</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A396810</td>
<td>Dog</td>
<td>2016-08-22 16:13:00</td>
<td>Injured</td>
<td>Raven</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A410668</td>
<td>Cat</td>
<td>2015-11-19 13:41:00</td>
<td>Normal</td>
<td>Raven</td>
<td>Spayed Female</td>
</tr>
</tbody>
      </table>
<ol>
<li>이름을 사전 순으로 정렬하면 다음과 같으며, 'Jewel', 'Raven', 'Sugar'</li>
<li>'Raven'이라는 이름을 가진 개와 고양이가 있으므로, 이 중에서는 보호를 나중에 시작한 개를 먼저 조회합니다.</li>
</ol>

<p>따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.</p>
<table class="table">
        <thead><tr>
<th>ANIMAL_ID</th>
<th>NAME</th>
<th>DATETIME</th>
</tr>
</thead>
        <tbody><tr>
<td>A350276</td>
<td>Jewel</td>
<td>2017-08-13 13:50:00</td>
</tr>
<tr>
<td>A396810</td>
<td>Raven</td>
<td>2016-08-22 16:13:00</td>
</tr>
<tr>
<td>A410668</td>
<td>Raven</td>
<td>2015-11-19 13:41:00</td>
</tr>
<tr>
<td>A349996</td>
<td>Sugar</td>
<td>2018-01-22 14:32:00</td>
</tr>
</tbody>
      </table>
<hr>

<p>본 문제는 <a href="https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes" target="_blank" rel="noopener">Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes"</a>에서 제공하는 데이터를 사용하였으며 <a href="https://opendatacommons.org/licenses/odbl/1.0/" target="_blank" rel="noopener">ODbL</a>의 적용을 받습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges