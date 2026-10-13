# 홈 히어로 제품 릴: 대표 컷 5장 크로스페이드 + 약한 줌 (Ken Burns 1.00 -> 1.04)
# 실행: 레포 루트에서  pwsh _tools/make_reel.ps1   (ffmpeg 필요)
# 마지막에 TS450 첫 프레임으로 다시 페이드해 루프가 이음새 없이 이어진다.
$ErrorActionPreference = 'Stop'
$imgs = @(
  'assets/works/ts450/cover_src.jpg',   # 수상작 TS450 (첫 컷 = poster)
  'assets/works/ts700/cover_src.jpg',
  'assets/works/h500/ctrl_living.jpg',
  'assets/works/wade/scene_print.jpg',
  'assets/works/mobilink/hero3.jpg'
)
$clip = 3.2; $fade = 0.6; $fps = 30; $n = [int]($clip * $fps)
$args = @()
foreach ($i in $imgs) { $args += @('-loop', '1', '-framerate', "$fps", '-t', "$clip", '-i', $i) }
$args += @('-loop', '1', '-framerate', "$fps", '-t', "$fade", '-i', $imgs[0])

$f = ''
for ($k = 0; $k -lt $imgs.Count; $k++) {
  $f += "[$($k):v]scale=3200:1800:force_original_aspect_ratio=increase,crop=3200:1800," +
        "zoompan=z='1+0.04*on/$($n - 1)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1600x900:fps=$fps," +
        "setsar=1,format=yuv420p[v$k];"
}
$last = $imgs.Count
$f += "[$($last):v]scale=1600:900:force_original_aspect_ratio=increase,crop=1600:900,setsar=1,fps=$fps,format=yuv420p[v$last];"
$prev = 'v0'; $off = 0.0
for ($k = 1; $k -le $last; $k++) {
  $off = [math]::Round($off + $clip - $fade, 3)
  $out = if ($k -eq $last) { 'out' } else { "x$k" }
  $f += "[$prev][v$k]xfade=transition=fade:duration=$($fade):offset=$($off)[$out];"
  $prev = $out
}
$f = $f.TrimEnd(';')

ffmpeg -y -loglevel error @args -filter_complex $f -map '[out]' -an -c:v libx264 -crf 26 -preset slow `
  -pix_fmt yuv420p -movflags +faststart assets/hero-reel.mp4
ffmpeg -y -loglevel error -i $imgs[0] -vf "scale=1600:900:force_original_aspect_ratio=increase,crop=1600:900" -q:v 4 assets/hero-reel-poster.jpg
"reel: {0:N2} MB" -f ((Get-Item assets/hero-reel.mp4).Length / 1MB)
ffprobe -v error -show_entries format=duration -of csv=p=0 assets/hero-reel.mp4
