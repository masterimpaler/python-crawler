<?php
include_once('simple_html_dom.php');
$html = new simple_html_dom();
$target_url = "http://www.jkuat.ac.ke";
$html->load_file($target_url);
foreach($html->find('a') as $link)
{
echo $link->href."<br />";
}
?>