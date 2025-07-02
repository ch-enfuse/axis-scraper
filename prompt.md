### 🧠 Context
I'm building a **RAG (Retrieval-Augmented Generation)** bot that feeds a vector database (OpenAI integration) with product documentation from **Axis Communications**.

---

### ✅ Objective
Write a **Python-based web crawler** that:

1. **Starts from**:  
   `https://www.axis.com/en-us/products`
from here you'll find this html to crawl through all categories
```html
<div class="products-collection"><div class="views-element-container"><h3 class="products-collection__title" data-gtm-vis-recent-on-screen31532331_296="552" data-gtm-vis-first-on-screen31532331_296="552" data-gtm-vis-total-visible-time31532331_296="3000" data-gtm-vis-has-fired31532331_296="1">Product categories </h3>
  <div class="nav-card__coll">
    
<a href="/en-us/products/network-cameras" data-history-node-id="335" class="nav-card nav-card--deck nav-card--large-img">
          <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2020-05/NetworkCameras3840x1536.jpg.webp?itok=CJu_xpIO 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2020-05/NetworkCameras3840x1536.jpg.webp?itok=X34-Oncu 2x" media="(min-width: 1360px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2020-05/NetworkCameras3840x1536.jpg.webp?itok=CJu_xpIO 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2020-05/NetworkCameras3840x1536.jpg.webp?itok=X34-Oncu 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2020-05/NetworkCameras3840x1536.jpg.webp?itok=CJu_xpIO 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2020-05/NetworkCameras3840x1536.jpg.webp?itok=X34-Oncu 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2020-05/NetworkCameras3840x1536.jpg.webp?itok=zWlHFwdb 1x, /sites/axis/files/styles/square_125x125_jpg/public/2020-05/NetworkCameras3840x1536.jpg.webp?itok=zWlHFwdb 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="125" height="125">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2020-05/NetworkCameras3840x1536.jpg.webp?itok=zWlHFwdb 1x, /sites/axis/files/styles/square_125x125_jpg/public/2020-05/NetworkCameras3840x1536.jpg.webp?itok=zWlHFwdb 2x" media="(max-width: 575px)" type="image/webp" width="125" height="125">
                  <img loading="eager" width="320" height="192" src="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2020-05/NetworkCameras3840x1536.jpg.webp?itok=CJu_xpIO" alt="Axis IP camera mounted on the wall">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4 data-gtm-vis-recent-on-screen31532331_296="1467" data-gtm-vis-first-on-screen31532331_296="1467" data-gtm-vis-total-visible-time31532331_296="3000" data-gtm-vis-has-fired31532331_296="1">Network cameras</h4>
        
    
      <span class="nav-card__tagline">The best in network video: innovation, quality and opportunity</span>
  
      </div>
  </a>

<a href="/en-us/products/network-intercoms" data-history-node-id="2832" class="nav-card nav-card--deck nav-card--large-img">
          <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2023-11/I8016_LVE_vandal_stone_2211_hi_High%20resolution%20%28jpeg%29%20%282%29.jpg.webp?itok=9HenaTCy 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2023-11/I8016_LVE_vandal_stone_2211_hi_High%20resolution%20%28jpeg%29%20%282%29.jpg.webp?itok=gYuZCZDq 2x" media="(min-width: 1360px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2023-11/I8016_LVE_vandal_stone_2211_hi_High%20resolution%20%28jpeg%29%20%282%29.jpg.webp?itok=9HenaTCy 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2023-11/I8016_LVE_vandal_stone_2211_hi_High%20resolution%20%28jpeg%29%20%282%29.jpg.webp?itok=gYuZCZDq 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2023-11/I8016_LVE_vandal_stone_2211_hi_High%20resolution%20%28jpeg%29%20%282%29.jpg.webp?itok=9HenaTCy 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2023-11/I8016_LVE_vandal_stone_2211_hi_High%20resolution%20%28jpeg%29%20%282%29.jpg.webp?itok=gYuZCZDq 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2023-11/I8016_LVE_vandal_stone_2211_hi_High%20resolution%20%28jpeg%29%20%282%29.jpg.webp?itok=zp2_1-Gu 1x, /sites/axis/files/styles/square_125x125_jpg/public/2023-11/I8016_LVE_vandal_stone_2211_hi_High%20resolution%20%28jpeg%29%20%282%29.jpg.webp?itok=zp2_1-Gu 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="125" height="125">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2023-11/I8016_LVE_vandal_stone_2211_hi_High%20resolution%20%28jpeg%29%20%282%29.jpg.webp?itok=zp2_1-Gu 1x, /sites/axis/files/styles/square_125x125_jpg/public/2023-11/I8016_LVE_vandal_stone_2211_hi_High%20resolution%20%28jpeg%29%20%282%29.jpg.webp?itok=zp2_1-Gu 2x" media="(max-width: 575px)" type="image/webp" width="125" height="125">
                  <img loading="eager" width="320" height="192" src="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2023-11/I8016_LVE_vandal_stone_2211_hi_High%20resolution%20%28jpeg%29%20%282%29.jpg.webp?itok=9HenaTCy" alt="I8016-LVE">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4 data-gtm-vis-recent-on-screen31532331_296="1467" data-gtm-vis-first-on-screen31532331_296="1467" data-gtm-vis-total-visible-time31532331_296="3000" data-gtm-vis-has-fired31532331_296="1">Network intercoms</h4>
        
    
      <span class="nav-card__tagline">Smart and secure intercom solutions</span>
  
      </div>
  </a>

<a href="/en-us/products/access-control" data-history-node-id="2830" class="nav-card nav-card--deck nav-card--large-img">
          <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2023-01/access_control_a4120ve_1_3840x1536_2301.jpg.webp?itok=tAqmyVay 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2023-01/access_control_a4120ve_1_3840x1536_2301.jpg.webp?itok=TDQ07KUt 2x" media="(min-width: 1360px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2023-01/access_control_a4120ve_1_3840x1536_2301.jpg.webp?itok=tAqmyVay 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2023-01/access_control_a4120ve_1_3840x1536_2301.jpg.webp?itok=TDQ07KUt 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2023-01/access_control_a4120ve_1_3840x1536_2301.jpg.webp?itok=tAqmyVay 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2023-01/access_control_a4120ve_1_3840x1536_2301.jpg.webp?itok=TDQ07KUt 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2023-01/access_control_a4120ve_1_3840x1536_2301.jpg.webp?itok=IzPhujdB 1x, /sites/axis/files/styles/square_125x125_jpg/public/2023-01/access_control_a4120ve_1_3840x1536_2301.jpg.webp?itok=IzPhujdB 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="125" height="125">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2023-01/access_control_a4120ve_1_3840x1536_2301.jpg.webp?itok=IzPhujdB 1x, /sites/axis/files/styles/square_125x125_jpg/public/2023-01/access_control_a4120ve_1_3840x1536_2301.jpg.webp?itok=IzPhujdB 2x" media="(max-width: 575px)" type="image/webp" width="125" height="125">
                  <img loading="eager" width="320" height="192" src="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2023-01/access_control_a4120ve_1_3840x1536_2301.jpg.webp?itok=tAqmyVay" alt="access control, hand holding a card to enter the door">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4 data-gtm-vis-recent-on-screen31532331_296="1467" data-gtm-vis-first-on-screen31532331_296="1467" data-gtm-vis-total-visible-time31532331_296="3000" data-gtm-vis-has-fired31532331_296="1">Access control</h4>
        
    
      <span class="nav-card__tagline">Flexible access control – more than just open</span>
  
      </div>
  </a>

<a href="/en-us/products/network-audio" data-history-node-id="2833" class="nav-card nav-card--deck nav-card--large-img">
          <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2024-06/top_banner_c1110e_3840x1000_2406.jpg.webp?itok=YZsFSKe0 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2024-06/top_banner_c1110e_3840x1000_2406.jpg.webp?itok=qvnthrUW 2x" media="(min-width: 1360px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2024-06/top_banner_c1110e_3840x1000_2406.jpg.webp?itok=YZsFSKe0 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2024-06/top_banner_c1110e_3840x1000_2406.jpg.webp?itok=qvnthrUW 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2024-06/top_banner_c1110e_3840x1000_2406.jpg.webp?itok=YZsFSKe0 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2024-06/top_banner_c1110e_3840x1000_2406.jpg.webp?itok=qvnthrUW 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2024-06/top_banner_c1110e_3840x1000_2406.jpg.webp?itok=REIqCgMN 1x, /sites/axis/files/styles/square_125x125_jpg/public/2024-06/top_banner_c1110e_3840x1000_2406.jpg.webp?itok=REIqCgMN 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="125" height="125">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2024-06/top_banner_c1110e_3840x1000_2406.jpg.webp?itok=REIqCgMN 1x, /sites/axis/files/styles/square_125x125_jpg/public/2024-06/top_banner_c1110e_3840x1000_2406.jpg.webp?itok=REIqCgMN 2x" media="(max-width: 575px)" type="image/webp" width="125" height="125">
                  <img loading="eager" width="320" height="192" src="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2024-06/top_banner_c1110e_3840x1000_2406.jpg.webp?itok=YZsFSKe0" alt="Network Cabinet speaker">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4 data-gtm-vis-first-on-screen31532331_296="1467" data-gtm-vis-total-visible-time31532331_296="1500">Network audio</h4>
        
    
      <span class="nav-card__tagline">Audio made smart and easy</span>
  
      </div>
  </a>

<a href="/en-us/products/wearables" data-history-node-id="2815" class="nav-card nav-card--deck nav-card--large-img">
          <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2022-02/bw_wearables_3840x1536.jpg.webp?itok=O2RFgVwq 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2022-02/bw_wearables_3840x1536.jpg.webp?itok=6_XNjCm4 2x" media="(min-width: 1360px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2022-02/bw_wearables_3840x1536.jpg.webp?itok=O2RFgVwq 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2022-02/bw_wearables_3840x1536.jpg.webp?itok=6_XNjCm4 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2022-02/bw_wearables_3840x1536.jpg.webp?itok=O2RFgVwq 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2022-02/bw_wearables_3840x1536.jpg.webp?itok=6_XNjCm4 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2022-02/bw_wearables_3840x1536.jpg.webp?itok=001rt4fU 1x, /sites/axis/files/styles/square_125x125_jpg/public/2022-02/bw_wearables_3840x1536.jpg.webp?itok=001rt4fU 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="125" height="125">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2022-02/bw_wearables_3840x1536.jpg.webp?itok=001rt4fU 1x, /sites/axis/files/styles/square_125x125_jpg/public/2022-02/bw_wearables_3840x1536.jpg.webp?itok=001rt4fU 2x" media="(max-width: 575px)" type="image/webp" width="125" height="125">
                  <img loading="eager" width="320" height="192" src="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2022-02/bw_wearables_3840x1536.jpg.webp?itok=O2RFgVwq" alt="body worn wearables battery">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4>Wearables</h4>
        
    
      <span class="nav-card__tagline">Open-platform body worn cameras</span>
  
      </div>
  </a>

<a href="/en-us/products/video-recorders-and-workstations" data-history-node-id="2606" class="nav-card nav-card--deck nav-card--large-img">
          <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2021-05/MicrosoftTeams-image%20%2814%29.png.webp?itok=nqrnG06n 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2021-05/MicrosoftTeams-image%20%2814%29.png.webp?itok=E0xdi-Xe 2x" media="(min-width: 1360px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2021-05/MicrosoftTeams-image%20%2814%29.png.webp?itok=nqrnG06n 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2021-05/MicrosoftTeams-image%20%2814%29.png.webp?itok=E0xdi-Xe 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2021-05/MicrosoftTeams-image%20%2814%29.png.webp?itok=nqrnG06n 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2021-05/MicrosoftTeams-image%20%2814%29.png.webp?itok=E0xdi-Xe 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2021-05/MicrosoftTeams-image%20%2814%29.png.webp?itok=IvkO-Hvt 1x, /sites/axis/files/styles/square_125x125_jpg/public/2021-05/MicrosoftTeams-image%20%2814%29.png.webp?itok=IvkO-Hvt 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="125" height="125">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2021-05/MicrosoftTeams-image%20%2814%29.png.webp?itok=IvkO-Hvt 1x, /sites/axis/files/styles/square_125x125_jpg/public/2021-05/MicrosoftTeams-image%20%2814%29.png.webp?itok=IvkO-Hvt 2x" media="(max-width: 575px)" type="image/webp" width="125" height="125">
                  <img loading="eager" width="320" height="192" src="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2021-05/MicrosoftTeams-image%20%2814%29.png.webp?itok=nqrnG06n" alt="photo of server">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4>Video recorders and workstations</h4>
        
    
      <span class="nav-card__tagline">Out-of-the-box ready recording solutions</span>
  
      </div>
  </a>

<a href="/en-us/products/system-devices" data-history-node-id="2536" class="nav-card nav-card--deck nav-card--large-img">
          <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2023-07/top_banner_switch_t85_08_16_24_family_3840x1536_2307%20%281%29.jpg.webp?itok=oyICCveK 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2023-07/top_banner_switch_t85_08_16_24_family_3840x1536_2307%20%281%29.jpg.webp?itok=gZm_zS4S 2x" media="(min-width: 1360px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2023-07/top_banner_switch_t85_08_16_24_family_3840x1536_2307%20%281%29.jpg.webp?itok=oyICCveK 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2023-07/top_banner_switch_t85_08_16_24_family_3840x1536_2307%20%281%29.jpg.webp?itok=gZm_zS4S 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2023-07/top_banner_switch_t85_08_16_24_family_3840x1536_2307%20%281%29.jpg.webp?itok=oyICCveK 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2023-07/top_banner_switch_t85_08_16_24_family_3840x1536_2307%20%281%29.jpg.webp?itok=gZm_zS4S 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2023-07/top_banner_switch_t85_08_16_24_family_3840x1536_2307%20%281%29.jpg.webp?itok=qRX-uBrp 1x, /sites/axis/files/styles/square_125x125_jpg/public/2023-07/top_banner_switch_t85_08_16_24_family_3840x1536_2307%20%281%29.jpg.webp?itok=qRX-uBrp 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="125" height="125">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2023-07/top_banner_switch_t85_08_16_24_family_3840x1536_2307%20%281%29.jpg.webp?itok=qRX-uBrp 1x, /sites/axis/files/styles/square_125x125_jpg/public/2023-07/top_banner_switch_t85_08_16_24_family_3840x1536_2307%20%281%29.jpg.webp?itok=qRX-uBrp 2x" media="(max-width: 575px)" type="image/webp" width="125" height="125">
                  <img loading="eager" width="320" height="192" src="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2023-07/top_banner_switch_t85_08_16_24_family_3840x1536_2307%20%281%29.jpg.webp?itok=oyICCveK" alt="AXIS T85 Series switches">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4>System devices</h4>
        
    
      <span class="nav-card__tagline">Components for intelligent systems</span>
  
      </div>
  </a>

<a href="/en-us/products/accessories" data-history-node-id="2608" class="nav-card nav-card--deck nav-card--large-img">
          <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2020-06/Accessories3840x1536.jpg.webp?itok=U_9J-sA2 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2020-06/Accessories3840x1536.jpg.webp?itok=cQ_vFq0e 2x" media="(min-width: 1360px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2020-06/Accessories3840x1536.jpg.webp?itok=U_9J-sA2 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2020-06/Accessories3840x1536.jpg.webp?itok=cQ_vFq0e 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2020-06/Accessories3840x1536.jpg.webp?itok=U_9J-sA2 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2020-06/Accessories3840x1536.jpg.webp?itok=cQ_vFq0e 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2020-06/Accessories3840x1536.jpg.webp?itok=ZVG_4nCq 1x, /sites/axis/files/styles/square_125x125_jpg/public/2020-06/Accessories3840x1536.jpg.webp?itok=ZVG_4nCq 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="125" height="125">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2020-06/Accessories3840x1536.jpg.webp?itok=ZVG_4nCq 1x, /sites/axis/files/styles/square_125x125_jpg/public/2020-06/Accessories3840x1536.jpg.webp?itok=ZVG_4nCq 2x" media="(max-width: 575px)" type="image/webp" width="125" height="125">
                  <img loading="eager" width="320" height="192" src="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2020-06/Accessories3840x1536.jpg.webp?itok=U_9J-sA2" alt="Axis IP camera mounted in the ceiling">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4>Accessories</h4>
        
    
      <span class="nav-card__tagline">Everything you need to complete your systems</span>
  
      </div>
  </a>

<a href="/en-us/products/analytics" data-history-node-id="2831" class="nav-card nav-card--deck nav-card--large-img">
          <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2025-01/top_banner_axis_analytics_3840x1000_2501.jpg.webp?itok=R7OFsd5V 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2025-01/top_banner_axis_analytics_3840x1000_2501.jpg.webp?itok=nSN8k8H_ 2x" media="(min-width: 1360px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2025-01/top_banner_axis_analytics_3840x1000_2501.jpg.webp?itok=R7OFsd5V 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2025-01/top_banner_axis_analytics_3840x1000_2501.jpg.webp?itok=nSN8k8H_ 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2025-01/top_banner_axis_analytics_3840x1000_2501.jpg.webp?itok=R7OFsd5V 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2025-01/top_banner_axis_analytics_3840x1000_2501.jpg.webp?itok=nSN8k8H_ 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2025-01/top_banner_axis_analytics_3840x1000_2501.jpg.webp?itok=CbiDF5uv 1x, /sites/axis/files/styles/square_125x125_jpg/public/2025-01/top_banner_axis_analytics_3840x1000_2501.jpg.webp?itok=CbiDF5uv 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="125" height="125">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2025-01/top_banner_axis_analytics_3840x1000_2501.jpg.webp?itok=CbiDF5uv 1x, /sites/axis/files/styles/square_125x125_jpg/public/2025-01/top_banner_axis_analytics_3840x1000_2501.jpg.webp?itok=CbiDF5uv 2x" media="(max-width: 575px)" type="image/webp" width="125" height="125">
                  <img loading="eager" width="320" height="192" src="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2025-01/top_banner_axis_analytics_3840x1000_2501.jpg.webp?itok=R7OFsd5V" alt="Axis analytics solutions">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4>Analytics</h4>
        
    
      <span class="nav-card__tagline">Easy access to actionable insights </span>
  
      </div>
  </a>

<a href="/en-us/products/explosion-protected-devices" data-history-node-id="54801" class="nav-card nav-card--deck nav-card--large-img">
          <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2024-08/xfq1656_hazardous_area_04_2304_3840x1000_0.jpg.webp?itok=B6AOWql7 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2024-08/xfq1656_hazardous_area_04_2304_3840x1000_0.jpg.webp?itok=ihE2RWPd 2x" media="(min-width: 1360px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2024-08/xfq1656_hazardous_area_04_2304_3840x1000_0.jpg.webp?itok=B6AOWql7 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2024-08/xfq1656_hazardous_area_04_2304_3840x1000_0.jpg.webp?itok=ihE2RWPd 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2024-08/xfq1656_hazardous_area_04_2304_3840x1000_0.jpg.webp?itok=B6AOWql7 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2024-08/xfq1656_hazardous_area_04_2304_3840x1000_0.jpg.webp?itok=ihE2RWPd 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2024-08/xfq1656_hazardous_area_04_2304_3840x1000_0.jpg.webp?itok=eldAa-Nf 1x, /sites/axis/files/styles/square_125x125_jpg/public/2024-08/xfq1656_hazardous_area_04_2304_3840x1000_0.jpg.webp?itok=eldAa-Nf 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="125" height="125">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2024-08/xfq1656_hazardous_area_04_2304_3840x1000_0.jpg.webp?itok=eldAa-Nf 1x, /sites/axis/files/styles/square_125x125_jpg/public/2024-08/xfq1656_hazardous_area_04_2304_3840x1000_0.jpg.webp?itok=eldAa-Nf 2x" media="(max-width: 575px)" type="image/webp" width="125" height="125">
                  <img loading="eager" width="320" height="192" src="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2024-08/xfq1656_hazardous_area_04_2304_3840x1000_0.jpg.webp?itok=B6AOWql7" alt="xfq1656 hazardous area">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4>Explosion-protected devices</h4>
        
    
      <span class="nav-card__tagline">Certified for hazardous areas</span>
  
      </div>
  </a>

<a href="/en-us/products/management-software" data-history-node-id="55749" class="nav-card nav-card--deck nav-card--large-img">
          <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2024-12/laptop_hands_management_software_3840x1000_2411.png.webp?itok=JhjH5Ibn 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2024-12/laptop_hands_management_software_3840x1000_2411.png.webp?itok=l4YpiRKU 2x" media="(min-width: 1360px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2024-12/laptop_hands_management_software_3840x1000_2411.png.webp?itok=JhjH5Ibn 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2024-12/laptop_hands_management_software_3840x1000_2411.png.webp?itok=l4YpiRKU 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2024-12/laptop_hands_management_software_3840x1000_2411.png.webp?itok=JhjH5Ibn 1x, /sites/axis/files/styles/landscape_640_x_384_jpg/public/2024-12/laptop_hands_management_software_3840x1000_2411.png.webp?itok=l4YpiRKU 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="320" height="192">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2024-12/laptop_hands_management_software_3840x1000_2411.png.webp?itok=eOeUuWmB 1x, /sites/axis/files/styles/square_125x125_jpg/public/2024-12/laptop_hands_management_software_3840x1000_2411.png.webp?itok=eOeUuWmB 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="125" height="125">
              <source srcset="/sites/axis/files/styles/square_125x125_jpg/public/2024-12/laptop_hands_management_software_3840x1000_2411.png.webp?itok=eOeUuWmB 1x, /sites/axis/files/styles/square_125x125_jpg/public/2024-12/laptop_hands_management_software_3840x1000_2411.png.webp?itok=eOeUuWmB 2x" media="(max-width: 575px)" type="image/webp" width="125" height="125">
                  <img loading="eager" width="320" height="192" src="/sites/axis/files/styles/landscape_320_x_192_jpg/public/2024-12/laptop_hands_management_software_3840x1000_2411.png.webp?itok=JhjH5Ibn" alt="Laptop security management software">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4>Management software</h4>
        
    
      <span class="nav-card__tagline">Helping you stay in control</span>
  
      </div>
  </a>

  </div>
</div>
</div>
```

2. Then go into all the categires like "Network Cameras"
   - ➤ Category pages (e.g.):  
     `https://www.axis.com/en-us/products/network-cameras`

from here you'l find this html
```html
<div class="views-element-container">



    <h3 data-gtm-vis-recent-on-screen31532331_296="291" data-gtm-vis-first-on-screen31532331_296="291" data-gtm-vis-total-visible-time31532331_296="3000" data-gtm-vis-has-fired31532331_296="1">Collections within NETWORK CAMERAS</h3>
    <div class="nav-card__coll">
    
<a href="/en-us/products/dome-cameras" data-history-node-id="338" class="nav-card nav-card--deck">
        
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-09/p3268_lve_w_weathershield_wall_angle_left_2112-Productimage.png.webp?itok=9SUMl_9z 1x, /sites/axis/files/styles/square_300x300_white/public/2022-09/p3268_lve_w_weathershield_wall_angle_left_2112-Productimage.png.webp?itok=MY7wz8GQ 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-09/p3268_lve_w_weathershield_wall_angle_left_2112-Productimage.png.webp?itok=9SUMl_9z 1x, /sites/axis/files/styles/square_300x300_white/public/2022-09/p3268_lve_w_weathershield_wall_angle_left_2112-Productimage.png.webp?itok=MY7wz8GQ 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-09/p3268_lve_w_weathershield_wall_angle_left_2112-Productimage.png.webp?itok=9SUMl_9z 1x, /sites/axis/files/styles/square_300x300_white/public/2022-09/p3268_lve_w_weathershield_wall_angle_left_2112-Productimage.png.webp?itok=MY7wz8GQ 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2022-09/p3268_lve_w_weathershield_wall_angle_left_2112-Productimage.png.webp?itok=iPGWMmQX 1x, /sites/axis/files/styles/square_160x160_white/public/2022-09/p3268_lve_w_weathershield_wall_angle_left_2112-Productimage.png.webp?itok=9SUMl_9z 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2022-09/p3268_lve_w_weathershield_wall_angle_left_2112-Productimage.png.webp?itok=iPGWMmQX 1x, /sites/axis/files/styles/square_160x160_white/public/2022-09/p3268_lve_w_weathershield_wall_angle_left_2112-Productimage.png.webp?itok=9SUMl_9z 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2022-09/p3268_lve_w_weathershield_wall_angle_left_2112-Productimage.png.webp?itok=9SUMl_9z" alt="AXIS P3268-LVE viewed from its left">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4 data-gtm-vis-recent-on-screen31532331_296="1374" data-gtm-vis-first-on-screen31532331_296="1375" data-gtm-vis-total-visible-time31532331_296="3000" data-gtm-vis-has-fired31532331_296="1">Dome cameras</h4>
        
    
      <span class="nav-card__tagline">Discreet and solid in any environment</span>
  
      </div>
  </a>

<a href="/en-us/products/box-cameras" data-history-node-id="336" class="nav-card nav-card--deck">
        
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-01/p1388le_wall_angle_left_2312_Productimageswithcropping.png.webp?itok=a4zM9bfZ 1x, /sites/axis/files/styles/square_300x300_white/public/2025-01/p1388le_wall_angle_left_2312_Productimageswithcropping.png.webp?itok=XDxoYcSJ 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-01/p1388le_wall_angle_left_2312_Productimageswithcropping.png.webp?itok=a4zM9bfZ 1x, /sites/axis/files/styles/square_300x300_white/public/2025-01/p1388le_wall_angle_left_2312_Productimageswithcropping.png.webp?itok=XDxoYcSJ 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-01/p1388le_wall_angle_left_2312_Productimageswithcropping.png.webp?itok=a4zM9bfZ 1x, /sites/axis/files/styles/square_300x300_white/public/2025-01/p1388le_wall_angle_left_2312_Productimageswithcropping.png.webp?itok=XDxoYcSJ 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2025-01/p1388le_wall_angle_left_2312_Productimageswithcropping.png.webp?itok=2hkw0P7h 1x, /sites/axis/files/styles/square_160x160_white/public/2025-01/p1388le_wall_angle_left_2312_Productimageswithcropping.png.webp?itok=a4zM9bfZ 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2025-01/p1388le_wall_angle_left_2312_Productimageswithcropping.png.webp?itok=2hkw0P7h 1x, /sites/axis/files/styles/square_160x160_white/public/2025-01/p1388le_wall_angle_left_2312_Productimageswithcropping.png.webp?itok=a4zM9bfZ 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2025-01/p1388le_wall_angle_left_2312_Productimageswithcropping.png.webp?itok=a4zM9bfZ" alt="Axis box camera looking left on white background">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4 data-gtm-vis-recent-on-screen31532331_296="1375" data-gtm-vis-first-on-screen31532331_296="1375" data-gtm-vis-total-visible-time31532331_296="3000" data-gtm-vis-has-fired31532331_296="1">Box cameras</h4>
        
    
      <span class="nav-card__tagline">Deterrence in any environment</span>
  
      </div>
  </a>

<a href="/en-us/products/bullet-cameras" data-history-node-id="342" class="nav-card nav-card--deck">
        
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-04/q1795le_q1796le_angle_left_2212%20%288%29.png.webp?itok=WbxJt1LU 1x, /sites/axis/files/styles/square_300x300_white/public/2024-04/q1795le_q1796le_angle_left_2212%20%288%29.png.webp?itok=CBxg6XC2 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-04/q1795le_q1796le_angle_left_2212%20%288%29.png.webp?itok=WbxJt1LU 1x, /sites/axis/files/styles/square_300x300_white/public/2024-04/q1795le_q1796le_angle_left_2212%20%288%29.png.webp?itok=CBxg6XC2 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-04/q1795le_q1796le_angle_left_2212%20%288%29.png.webp?itok=WbxJt1LU 1x, /sites/axis/files/styles/square_300x300_white/public/2024-04/q1795le_q1796le_angle_left_2212%20%288%29.png.webp?itok=CBxg6XC2 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2024-04/q1795le_q1796le_angle_left_2212%20%288%29.png.webp?itok=g0KfVfQr 1x, /sites/axis/files/styles/square_160x160_white/public/2024-04/q1795le_q1796le_angle_left_2212%20%288%29.png.webp?itok=WbxJt1LU 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2024-04/q1795le_q1796le_angle_left_2212%20%288%29.png.webp?itok=g0KfVfQr 1x, /sites/axis/files/styles/square_160x160_white/public/2024-04/q1795le_q1796le_angle_left_2212%20%288%29.png.webp?itok=WbxJt1LU 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2024-04/q1795le_q1796le_angle_left_2212%20%288%29.png.webp?itok=WbxJt1LU" alt="AXIS Q18 Bullet Camera angle left">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4 data-gtm-vis-recent-on-screen31532331_296="1375" data-gtm-vis-first-on-screen31532331_296="1375" data-gtm-vis-total-visible-time31532331_296="3000" data-gtm-vis-has-fired31532331_296="1">Bullet cameras</h4>
        
    
      <span class="nav-card__tagline">For all purposes in any environment</span>
  
      </div>
  </a>

<a href="/en-us/products/ptz-cameras" data-history-node-id="409" class="nav-card nav-card--deck">
        
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2019-12/1600_q6125le-front-1802.png.webp?itok=DxgTrf3b 1x, /sites/axis/files/styles/square_300x300_white/public/2019-12/1600_q6125le-front-1802.png.webp?itok=4wN7foFh 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2019-12/1600_q6125le-front-1802.png.webp?itok=DxgTrf3b 1x, /sites/axis/files/styles/square_300x300_white/public/2019-12/1600_q6125le-front-1802.png.webp?itok=4wN7foFh 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2019-12/1600_q6125le-front-1802.png.webp?itok=DxgTrf3b 1x, /sites/axis/files/styles/square_300x300_white/public/2019-12/1600_q6125le-front-1802.png.webp?itok=4wN7foFh 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2019-12/1600_q6125le-front-1802.png.webp?itok=BRdyDXaq 1x, /sites/axis/files/styles/square_160x160_white/public/2019-12/1600_q6125le-front-1802.png.webp?itok=DxgTrf3b 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2019-12/1600_q6125le-front-1802.png.webp?itok=BRdyDXaq 1x, /sites/axis/files/styles/square_160x160_white/public/2019-12/1600_q6125le-front-1802.png.webp?itok=DxgTrf3b 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2019-12/1600_q6125le-front-1802.png.webp?itok=DxgTrf3b" alt="Axis IP Camera Q6125-LE has Built-in IR LEDs with OptimizedIR ">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4 data-gtm-vis-first-on-screen31532331_296="1375" data-gtm-vis-total-visible-time31532331_296="1400">PTZ cameras</h4>
        
    
      <span class="nav-card__tagline">Pan, tilt, and zoom capabilities for wide-area coverage </span>
  
      </div>
  </a>

<a href="/en-us/products/panoramic-cameras" data-history-node-id="340" class="nav-card nav-card--deck">
        
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-04/p3727ple_ceiling_angle_left_2106_1600x1600.png.webp?itok=ZQp98x3I 1x, /sites/axis/files/styles/square_300x300_white/public/2024-04/p3727ple_ceiling_angle_left_2106_1600x1600.png.webp?itok=cDVruoCs 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-04/p3727ple_ceiling_angle_left_2106_1600x1600.png.webp?itok=ZQp98x3I 1x, /sites/axis/files/styles/square_300x300_white/public/2024-04/p3727ple_ceiling_angle_left_2106_1600x1600.png.webp?itok=cDVruoCs 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-04/p3727ple_ceiling_angle_left_2106_1600x1600.png.webp?itok=ZQp98x3I 1x, /sites/axis/files/styles/square_300x300_white/public/2024-04/p3727ple_ceiling_angle_left_2106_1600x1600.png.webp?itok=cDVruoCs 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2024-04/p3727ple_ceiling_angle_left_2106_1600x1600.png.webp?itok=MC6H__Gk 1x, /sites/axis/files/styles/square_160x160_white/public/2024-04/p3727ple_ceiling_angle_left_2106_1600x1600.png.webp?itok=ZQp98x3I 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2024-04/p3727ple_ceiling_angle_left_2106_1600x1600.png.webp?itok=MC6H__Gk 1x, /sites/axis/files/styles/square_160x160_white/public/2024-04/p3727ple_ceiling_angle_left_2106_1600x1600.png.webp?itok=ZQp98x3I 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2024-04/p3727ple_ceiling_angle_left_2106_1600x1600.png.webp?itok=ZQp98x3I" alt="AXIS P3727-PLE Panoramic Camera, viewed from its left angle">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4>Panoramic cameras</h4>
        
    
      <span class="nav-card__tagline">Complete situational awareness with just one camera</span>
  
      </div>
  </a>

<a href="/en-us/products/modular-cameras" data-history-node-id="424" class="nav-card nav-card--deck">
        
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-05/modular_cameras_all_products_group%20%281%29.png.webp?itok=xOJrFmPF 1x, /sites/axis/files/styles/square_300x300_white/public/2025-05/modular_cameras_all_products_group%20%281%29.png.webp?itok=uMPpiDRN 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-05/modular_cameras_all_products_group%20%281%29.png.webp?itok=xOJrFmPF 1x, /sites/axis/files/styles/square_300x300_white/public/2025-05/modular_cameras_all_products_group%20%281%29.png.webp?itok=uMPpiDRN 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-05/modular_cameras_all_products_group%20%281%29.png.webp?itok=xOJrFmPF 1x, /sites/axis/files/styles/square_300x300_white/public/2025-05/modular_cameras_all_products_group%20%281%29.png.webp?itok=uMPpiDRN 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2025-05/modular_cameras_all_products_group%20%281%29.png.webp?itok=5AfHjjB2 1x, /sites/axis/files/styles/square_160x160_white/public/2025-05/modular_cameras_all_products_group%20%281%29.png.webp?itok=xOJrFmPF 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2025-05/modular_cameras_all_products_group%20%281%29.png.webp?itok=5AfHjjB2 1x, /sites/axis/files/styles/square_160x160_white/public/2025-05/modular_cameras_all_products_group%20%281%29.png.webp?itok=xOJrFmPF 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2025-05/modular_cameras_all_products_group%20%281%29.png.webp?itok=xOJrFmPF" alt="Axis Modular Cameras category collection">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4>Modular cameras</h4>
        
    
      <span class="nav-card__tagline">Flexible system for a high level of discretion</span>
  
      </div>
  </a>

<a href="/en-us/products/explosion-protected-cameras" data-history-node-id="421" class="nav-card nav-card--deck">
        
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-02/xpq1785_p1468xle_packshot_2212-Productimageswithcropping.png.webp?itok=7ZJZOYM0 1x, /sites/axis/files/styles/square_300x300_white/public/2023-02/xpq1785_p1468xle_packshot_2212-Productimageswithcropping.png.webp?itok=oVymICy8 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-02/xpq1785_p1468xle_packshot_2212-Productimageswithcropping.png.webp?itok=7ZJZOYM0 1x, /sites/axis/files/styles/square_300x300_white/public/2023-02/xpq1785_p1468xle_packshot_2212-Productimageswithcropping.png.webp?itok=oVymICy8 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-02/xpq1785_p1468xle_packshot_2212-Productimageswithcropping.png.webp?itok=7ZJZOYM0 1x, /sites/axis/files/styles/square_300x300_white/public/2023-02/xpq1785_p1468xle_packshot_2212-Productimageswithcropping.png.webp?itok=oVymICy8 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2023-02/xpq1785_p1468xle_packshot_2212-Productimageswithcropping.png.webp?itok=mDp7Q94w 1x, /sites/axis/files/styles/square_160x160_white/public/2023-02/xpq1785_p1468xle_packshot_2212-Productimageswithcropping.png.webp?itok=7ZJZOYM0 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2023-02/xpq1785_p1468xle_packshot_2212-Productimageswithcropping.png.webp?itok=mDp7Q94w 1x, /sites/axis/files/styles/square_160x160_white/public/2023-02/xpq1785_p1468xle_packshot_2212-Productimageswithcropping.png.webp?itok=7ZJZOYM0 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2023-02/xpq1785_p1468xle_packshot_2212-Productimageswithcropping.png.webp?itok=7ZJZOYM0" alt="Explosion-protected cameras from Axis">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4>Explosion-protected cameras</h4>
        
    
      <span class="nav-card__tagline">Certified for hazardous areas</span>
  
      </div>
  </a>

<a href="/en-us/products/onboard-cameras" data-history-node-id="425" class="nav-card nav-card--deck">
        
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-09/m3905r_p3905r_angle_left_2211-Productimageswithcropping.png.webp?itok=AEAGAsnP 1x, /sites/axis/files/styles/square_300x300_white/public/2023-09/m3905r_p3905r_angle_left_2211-Productimageswithcropping.png.webp?itok=m453JIpx 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-09/m3905r_p3905r_angle_left_2211-Productimageswithcropping.png.webp?itok=AEAGAsnP 1x, /sites/axis/files/styles/square_300x300_white/public/2023-09/m3905r_p3905r_angle_left_2211-Productimageswithcropping.png.webp?itok=m453JIpx 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-09/m3905r_p3905r_angle_left_2211-Productimageswithcropping.png.webp?itok=AEAGAsnP 1x, /sites/axis/files/styles/square_300x300_white/public/2023-09/m3905r_p3905r_angle_left_2211-Productimageswithcropping.png.webp?itok=m453JIpx 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2023-09/m3905r_p3905r_angle_left_2211-Productimageswithcropping.png.webp?itok=vjSFilHS 1x, /sites/axis/files/styles/square_160x160_white/public/2023-09/m3905r_p3905r_angle_left_2211-Productimageswithcropping.png.webp?itok=AEAGAsnP 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2023-09/m3905r_p3905r_angle_left_2211-Productimageswithcropping.png.webp?itok=vjSFilHS 1x, /sites/axis/files/styles/square_160x160_white/public/2023-09/m3905r_p3905r_angle_left_2211-Productimageswithcropping.png.webp?itok=AEAGAsnP 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2023-09/m3905r_p3905r_angle_left_2211-Productimageswithcropping.png.webp?itok=AEAGAsnP" alt="AXIS P3905-R Mk III">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4>Onboard cameras</h4>
        
    
      <span class="nav-card__tagline">For use on vehicles and rolling stock</span>
  
      </div>
  </a>

<a href="/en-us/products/thermal-cameras" data-history-node-id="343" class="nav-card nav-card--deck">
        
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-03/q1961te_wall_angle_left_2207-Productimage.png.webp?itok=Ua8d3tNz 1x, /sites/axis/files/styles/square_300x300_white/public/2023-03/q1961te_wall_angle_left_2207-Productimage.png.webp?itok=QmkIaYn_ 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-03/q1961te_wall_angle_left_2207-Productimage.png.webp?itok=Ua8d3tNz 1x, /sites/axis/files/styles/square_300x300_white/public/2023-03/q1961te_wall_angle_left_2207-Productimage.png.webp?itok=QmkIaYn_ 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-03/q1961te_wall_angle_left_2207-Productimage.png.webp?itok=Ua8d3tNz 1x, /sites/axis/files/styles/square_300x300_white/public/2023-03/q1961te_wall_angle_left_2207-Productimage.png.webp?itok=QmkIaYn_ 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2023-03/q1961te_wall_angle_left_2207-Productimage.png.webp?itok=jtNvrZdT 1x, /sites/axis/files/styles/square_160x160_white/public/2023-03/q1961te_wall_angle_left_2207-Productimage.png.webp?itok=Ua8d3tNz 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2023-03/q1961te_wall_angle_left_2207-Productimage.png.webp?itok=jtNvrZdT 1x, /sites/axis/files/styles/square_160x160_white/public/2023-03/q1961te_wall_angle_left_2207-Productimage.png.webp?itok=Ua8d3tNz 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2023-03/q1961te_wall_angle_left_2207-Productimage.png.webp?itok=Ua8d3tNz" alt="AXIS Q1961-TE 76834 ">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4>Thermal cameras</h4>
        
    
      <span class="nav-card__tagline">Heat-based detection for property defense and temperature-reading</span>
  
      </div>
  </a>

<a href="/en-us/products/specialty-cameras" data-history-node-id="341" class="nav-card nav-card--deck">
        
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-08/q9307_wall_angle_left_2311-Productimageswithcropping.png.webp?itok=3g1531ys 1x, /sites/axis/files/styles/square_300x300_white/public/2024-08/q9307_wall_angle_left_2311-Productimageswithcropping.png.webp?itok=xaNRGWHU 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-08/q9307_wall_angle_left_2311-Productimageswithcropping.png.webp?itok=3g1531ys 1x, /sites/axis/files/styles/square_300x300_white/public/2024-08/q9307_wall_angle_left_2311-Productimageswithcropping.png.webp?itok=xaNRGWHU 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-08/q9307_wall_angle_left_2311-Productimageswithcropping.png.webp?itok=3g1531ys 1x, /sites/axis/files/styles/square_300x300_white/public/2024-08/q9307_wall_angle_left_2311-Productimageswithcropping.png.webp?itok=xaNRGWHU 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2024-08/q9307_wall_angle_left_2311-Productimageswithcropping.png.webp?itok=Z-pN-FhO 1x, /sites/axis/files/styles/square_160x160_white/public/2024-08/q9307_wall_angle_left_2311-Productimageswithcropping.png.webp?itok=3g1531ys 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2024-08/q9307_wall_angle_left_2311-Productimageswithcropping.png.webp?itok=Z-pN-FhO 1x, /sites/axis/files/styles/square_160x160_white/public/2024-08/q9307_wall_angle_left_2311-Productimageswithcropping.png.webp?itok=3g1531ys 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2024-08/q9307_wall_angle_left_2311-Productimageswithcropping.png.webp?itok=3g1531ys" alt="AXIS Q9307-LV ">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4>Specialty cameras</h4>
        
    
      <span class="nav-card__tagline">For unique needs and scenarios</span>
  
      </div>
  </a>

<a href="/en-us/products/canon-network-cameras" data-history-node-id="2811" class="nav-card nav-card--deck">
        
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-11/24_vbh41b-12_path_2600x1920-Productimage.png.webp?itok=NeI2IrCw 1x, /sites/axis/files/styles/square_300x300_white/public/2022-11/24_vbh41b-12_path_2600x1920-Productimage.png.webp?itok=ZyZ8UZjM 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-11/24_vbh41b-12_path_2600x1920-Productimage.png.webp?itok=NeI2IrCw 1x, /sites/axis/files/styles/square_300x300_white/public/2022-11/24_vbh41b-12_path_2600x1920-Productimage.png.webp?itok=ZyZ8UZjM 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-11/24_vbh41b-12_path_2600x1920-Productimage.png.webp?itok=NeI2IrCw 1x, /sites/axis/files/styles/square_300x300_white/public/2022-11/24_vbh41b-12_path_2600x1920-Productimage.png.webp?itok=ZyZ8UZjM 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2022-11/24_vbh41b-12_path_2600x1920-Productimage.png.webp?itok=ce3rNKuK 1x, /sites/axis/files/styles/square_160x160_white/public/2022-11/24_vbh41b-12_path_2600x1920-Productimage.png.webp?itok=NeI2IrCw 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2022-11/24_vbh41b-12_path_2600x1920-Productimage.png.webp?itok=ce3rNKuK 1x, /sites/axis/files/styles/square_160x160_white/public/2022-11/24_vbh41b-12_path_2600x1920-Productimage.png.webp?itok=NeI2IrCw 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2022-11/24_vbh41b-12_path_2600x1920-Productimage.png.webp?itok=NeI2IrCw" alt="vb-h41b canon black camera">

  </picture>



</div>

    <div class="nav-card__text">
    
          <h4>Canon network cameras</h4>
        
    
      <span class="nav-card__tagline">Axis sells and supports Canon network cameras in EMEA, USA, Canada, Australia and New Zealand</span>
  
      </div>
  </a>

  </div>





</div>
```
From here you can go to one of the collection pages. like "Dome Cameras"
   - ➤ Collection pages (e.g.):  
     `https://www.axis.com/en-us/products/dome-cameras`
then in dome cameras, you'll find this html

```html
<div class="views-element-container">



    <h3 data-gtm-vis-recent-on-screen31532331_296="513" data-gtm-vis-first-on-screen31532331_296="513" data-gtm-vis-total-visible-time31532331_296="3000" data-gtm-vis-has-fired31532331_296="1">Products within DOME CAMERAS</h3>
    <div class="nav-card__coll">
      <a href="/en-us/products/axis-m30-series" data-history-node-id="337" class="nav-card nav-card--deck">
  
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-09/m3086v_ceiling_angle_left_2112_0.png.webp?itok=VDYG_mGj 1x, /sites/axis/files/styles/square_300x300_white/public/2022-09/m3086v_ceiling_angle_left_2112_0.png.webp?itok=ZW9TlBJ3 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-09/m3086v_ceiling_angle_left_2112_0.png.webp?itok=VDYG_mGj 1x, /sites/axis/files/styles/square_300x300_white/public/2022-09/m3086v_ceiling_angle_left_2112_0.png.webp?itok=ZW9TlBJ3 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-09/m3086v_ceiling_angle_left_2112_0.png.webp?itok=VDYG_mGj 1x, /sites/axis/files/styles/square_300x300_white/public/2022-09/m3086v_ceiling_angle_left_2112_0.png.webp?itok=ZW9TlBJ3 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2022-09/m3086v_ceiling_angle_left_2112_0.png.webp?itok=J0vmwdda 1x, /sites/axis/files/styles/square_160x160_white/public/2022-09/m3086v_ceiling_angle_left_2112_0.png.webp?itok=VDYG_mGj 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2022-09/m3086v_ceiling_angle_left_2112_0.png.webp?itok=J0vmwdda 1x, /sites/axis/files/styles/square_160x160_white/public/2022-09/m3086v_ceiling_angle_left_2112_0.png.webp?itok=VDYG_mGj 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2022-09/m3086v_ceiling_angle_left_2112_0.png.webp?itok=VDYG_mGj" alt="AXIS M3086-V Dome Camera, viewed from its left angle">

  </picture>



</div>

  <div class="nav-card__text">
    
        <h4>AXIS M30 Dome Camera Series </h4>
        
    <span class="nav-card__product-count">
      5 Products
    </span>
    
      <span class="nav-card__tagline">Affordable mini domes</span>
  
  </div>
</a>
<a href="/en-us/products/axis-m31-series" data-history-node-id="390" class="nav-card nav-card--deck">
  
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-08/m3126_white_ceiling_angle_left_2406-Productimageswithcropping.png.webp?itok=oJung1w2 1x, /sites/axis/files/styles/square_300x300_white/public/2024-08/m3126_white_ceiling_angle_left_2406-Productimageswithcropping.png.webp?itok=A94WsNbK 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-08/m3126_white_ceiling_angle_left_2406-Productimageswithcropping.png.webp?itok=oJung1w2 1x, /sites/axis/files/styles/square_300x300_white/public/2024-08/m3126_white_ceiling_angle_left_2406-Productimageswithcropping.png.webp?itok=A94WsNbK 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-08/m3126_white_ceiling_angle_left_2406-Productimageswithcropping.png.webp?itok=oJung1w2 1x, /sites/axis/files/styles/square_300x300_white/public/2024-08/m3126_white_ceiling_angle_left_2406-Productimageswithcropping.png.webp?itok=A94WsNbK 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2024-08/m3126_white_ceiling_angle_left_2406-Productimageswithcropping.png.webp?itok=2BUTSVtd 1x, /sites/axis/files/styles/square_160x160_white/public/2024-08/m3126_white_ceiling_angle_left_2406-Productimageswithcropping.png.webp?itok=oJung1w2 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2024-08/m3126_white_ceiling_angle_left_2406-Productimageswithcropping.png.webp?itok=2BUTSVtd 1x, /sites/axis/files/styles/square_160x160_white/public/2024-08/m3126_white_ceiling_angle_left_2406-Productimageswithcropping.png.webp?itok=oJung1w2 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2024-08/m3126_white_ceiling_angle_left_2406-Productimageswithcropping.png.webp?itok=oJung1w2" alt="AXIS M31 Series turret style camera">

  </picture>



</div>

  <div class="nav-card__text">
    
        <h4>AXIS M31 Dome Camera Series</h4>
        
    <span class="nav-card__product-count">
      3 Products
    </span>
    
      <span class="nav-card__tagline">Affordable flat-faced domes</span>
  
  </div>
</a>
<a href="/en-us/products/axis-m32-series" data-history-node-id="392" class="nav-card nav-card--deck">
  
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-06/72994.png.webp?itok=gxzfJ1D4 1x, /sites/axis/files/styles/square_300x300_white/public/2022-06/72994.png.webp?itok=h-GGJ7pK 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-06/72994.png.webp?itok=gxzfJ1D4 1x, /sites/axis/files/styles/square_300x300_white/public/2022-06/72994.png.webp?itok=h-GGJ7pK 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-06/72994.png.webp?itok=gxzfJ1D4 1x, /sites/axis/files/styles/square_300x300_white/public/2022-06/72994.png.webp?itok=h-GGJ7pK 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2022-06/72994.png.webp?itok=PBf9p9RS 1x, /sites/axis/files/styles/square_160x160_white/public/2022-06/72994.png.webp?itok=gxzfJ1D4 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2022-06/72994.png.webp?itok=PBf9p9RS 1x, /sites/axis/files/styles/square_160x160_white/public/2022-06/72994.png.webp?itok=gxzfJ1D4 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2022-06/72994.png.webp?itok=gxzfJ1D4" alt="AXIS M3216-LVE in black and white, viewed from the right ">

  </picture>



</div>

  <div class="nav-card__text">
    
        <h4>AXIS M32 Dome Camera Series</h4>
        
    <span class="nav-card__product-count">
      2 Products
    </span>
    
      <span class="nav-card__tagline">All-around fixed focal domes</span>
  
  </div>
</a>
  <a href="/en-us/products/axis-m3905-r" data-history-node-id="52293" class="nav-card nav-card--single">
    <div class="nav-card__media">
              <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-03/m3905r_p3905r_angle_left_2211-Productimage_0.png.webp?itok=Q5xFH8YK 1x, /sites/axis/files/styles/square_300x300_white/public/2023-03/m3905r_p3905r_angle_left_2211-Productimage_0.png.webp?itok=KUQUSi6X 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-03/m3905r_p3905r_angle_left_2211-Productimage_0.png.webp?itok=Q5xFH8YK 1x, /sites/axis/files/styles/square_300x300_white/public/2023-03/m3905r_p3905r_angle_left_2211-Productimage_0.png.webp?itok=KUQUSi6X 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-03/m3905r_p3905r_angle_left_2211-Productimage_0.png.webp?itok=Q5xFH8YK 1x, /sites/axis/files/styles/square_300x300_white/public/2023-03/m3905r_p3905r_angle_left_2211-Productimage_0.png.webp?itok=KUQUSi6X 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2023-03/m3905r_p3905r_angle_left_2211-Productimage_0.png.webp?itok=KAhKdmRU 1x, /sites/axis/files/styles/square_160x160_white/public/2023-03/m3905r_p3905r_angle_left_2211-Productimage_0.png.webp?itok=Q5xFH8YK 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2023-03/m3905r_p3905r_angle_left_2211-Productimage_0.png.webp?itok=KAhKdmRU 1x, /sites/axis/files/styles/square_160x160_white/public/2023-03/m3905r_p3905r_angle_left_2211-Productimage_0.png.webp?itok=Q5xFH8YK 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2023-03/m3905r_p3905r_angle_left_2211-Productimage_0.png.webp?itok=Q5xFH8YK" alt="AXIS M3905-R Dome Camera">

  </picture>




    </div>
        <div class="nav-card__text">
      
              <h4>AXIS M3905-R Dome Camera</h4>
            
      
      <span class="nav-card__tagline">2 MP indoor onboard surveillance</span>
  
    </div>
  </a>
<a href="/en-us/products/axis-m42-series" data-history-node-id="393" class="nav-card nav-card--deck">
  
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-05/m4225_m4228_wall_angle_left_2401_Productimageswithcropping.png.webp?itok=MyfLoc3F 1x, /sites/axis/files/styles/square_300x300_white/public/2025-05/m4225_m4228_wall_angle_left_2401_Productimageswithcropping.png.webp?itok=qCk8Be4X 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-05/m4225_m4228_wall_angle_left_2401_Productimageswithcropping.png.webp?itok=MyfLoc3F 1x, /sites/axis/files/styles/square_300x300_white/public/2025-05/m4225_m4228_wall_angle_left_2401_Productimageswithcropping.png.webp?itok=qCk8Be4X 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-05/m4225_m4228_wall_angle_left_2401_Productimageswithcropping.png.webp?itok=MyfLoc3F 1x, /sites/axis/files/styles/square_300x300_white/public/2025-05/m4225_m4228_wall_angle_left_2401_Productimageswithcropping.png.webp?itok=qCk8Be4X 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2025-05/m4225_m4228_wall_angle_left_2401_Productimageswithcropping.png.webp?itok=kAq94cGv 1x, /sites/axis/files/styles/square_160x160_white/public/2025-05/m4225_m4228_wall_angle_left_2401_Productimageswithcropping.png.webp?itok=MyfLoc3F 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2025-05/m4225_m4228_wall_angle_left_2401_Productimageswithcropping.png.webp?itok=kAq94cGv 1x, /sites/axis/files/styles/square_160x160_white/public/2025-05/m4225_m4228_wall_angle_left_2401_Productimageswithcropping.png.webp?itok=MyfLoc3F 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2025-05/m4225_m4228_wall_angle_left_2401_Productimageswithcropping.png.webp?itok=MyfLoc3F" alt="AXIS M4225-LVE">

  </picture>



</div>

  <div class="nav-card__text">
    
        <h4>AXIS M42 Dome Camera Series</h4>
        
    <span class="nav-card__product-count">
      9 Products
    </span>
    
      <span class="nav-card__tagline">Affordable AI-powered varifocal domes</span>
  
  </div>
</a>
<a href="/en-us/products/axis-m43-series" data-history-node-id="51959" class="nav-card nav-card--deck">
  
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-01/m4318plve_angle_left_2208-Productimage%20%281%29.png.webp?itok=ydKWHzxu 1x, /sites/axis/files/styles/square_300x300_white/public/2023-01/m4318plve_angle_left_2208-Productimage%20%281%29.png.webp?itok=VHx6T2-d 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-01/m4318plve_angle_left_2208-Productimage%20%281%29.png.webp?itok=ydKWHzxu 1x, /sites/axis/files/styles/square_300x300_white/public/2023-01/m4318plve_angle_left_2208-Productimage%20%281%29.png.webp?itok=VHx6T2-d 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-01/m4318plve_angle_left_2208-Productimage%20%281%29.png.webp?itok=ydKWHzxu 1x, /sites/axis/files/styles/square_300x300_white/public/2023-01/m4318plve_angle_left_2208-Productimage%20%281%29.png.webp?itok=VHx6T2-d 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2023-01/m4318plve_angle_left_2208-Productimage%20%281%29.png.webp?itok=WRvgvXbe 1x, /sites/axis/files/styles/square_160x160_white/public/2023-01/m4318plve_angle_left_2208-Productimage%20%281%29.png.webp?itok=ydKWHzxu 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2023-01/m4318plve_angle_left_2208-Productimage%20%281%29.png.webp?itok=WRvgvXbe 1x, /sites/axis/files/styles/square_160x160_white/public/2023-01/m4318plve_angle_left_2208-Productimage%20%281%29.png.webp?itok=ydKWHzxu 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2023-01/m4318plve_angle_left_2208-Productimage%20%281%29.png.webp?itok=ydKWHzxu" alt="AXIS M4317-PLVE left">

  </picture>



</div>

  <div class="nav-card__text">
    
        <h4>AXIS M43 Panoramic Camera Series</h4>
        
    <span class="nav-card__product-count">
      7 Products
    </span>
    
      <span class="nav-card__tagline">Eagle-eyed intelligence</span>
  
  </div>
</a>
<a href="/en-us/products/axis-p32-series" data-history-node-id="395" class="nav-card nav-card--deck">
  
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-06/p3277lve_wall_angle_left_2412_Productimageswithcropping%20%281%29.png.webp?itok=QeawHjOa 1x, /sites/axis/files/styles/square_300x300_white/public/2025-06/p3277lve_wall_angle_left_2412_Productimageswithcropping%20%281%29.png.webp?itok=cnpf4ebk 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-06/p3277lve_wall_angle_left_2412_Productimageswithcropping%20%281%29.png.webp?itok=QeawHjOa 1x, /sites/axis/files/styles/square_300x300_white/public/2025-06/p3277lve_wall_angle_left_2412_Productimageswithcropping%20%281%29.png.webp?itok=cnpf4ebk 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-06/p3277lve_wall_angle_left_2412_Productimageswithcropping%20%281%29.png.webp?itok=QeawHjOa 1x, /sites/axis/files/styles/square_300x300_white/public/2025-06/p3277lve_wall_angle_left_2412_Productimageswithcropping%20%281%29.png.webp?itok=cnpf4ebk 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2025-06/p3277lve_wall_angle_left_2412_Productimageswithcropping%20%281%29.png.webp?itok=6d9nMiA0 1x, /sites/axis/files/styles/square_160x160_white/public/2025-06/p3277lve_wall_angle_left_2412_Productimageswithcropping%20%281%29.png.webp?itok=QeawHjOa 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2025-06/p3277lve_wall_angle_left_2412_Productimageswithcropping%20%281%29.png.webp?itok=6d9nMiA0 1x, /sites/axis/files/styles/square_160x160_white/public/2025-06/p3277lve_wall_angle_left_2412_Productimageswithcropping%20%281%29.png.webp?itok=QeawHjOa 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2025-06/p3277lve_wall_angle_left_2412_Productimageswithcropping%20%281%29.png.webp?itok=QeawHjOa" alt="AXIS P3277-LVE">

  </picture>



</div>

  <div class="nav-card__text">
    
        <h4>AXIS P32 Dome Camera Series</h4>
        
    <span class="nav-card__product-count">
      17 Products
    </span>
    
      <span class="nav-card__tagline">Versatile AI-powered domes</span>
  
  </div>
</a>
<a href="/en-us/products/axis-p39-series" data-history-node-id="356" class="nav-card nav-card--deck">
  
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-09/p3935lr_ceiling_angle_left_2001.png.webp?itok=k7qzzMqQ 1x, /sites/axis/files/styles/square_300x300_white/public/2022-09/p3935lr_ceiling_angle_left_2001.png.webp?itok=PK-2ebxn 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-09/p3935lr_ceiling_angle_left_2001.png.webp?itok=k7qzzMqQ 1x, /sites/axis/files/styles/square_300x300_white/public/2022-09/p3935lr_ceiling_angle_left_2001.png.webp?itok=PK-2ebxn 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2022-09/p3935lr_ceiling_angle_left_2001.png.webp?itok=k7qzzMqQ 1x, /sites/axis/files/styles/square_300x300_white/public/2022-09/p3935lr_ceiling_angle_left_2001.png.webp?itok=PK-2ebxn 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2022-09/p3935lr_ceiling_angle_left_2001.png.webp?itok=aUKmGPXB 1x, /sites/axis/files/styles/square_160x160_white/public/2022-09/p3935lr_ceiling_angle_left_2001.png.webp?itok=k7qzzMqQ 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2022-09/p3935lr_ceiling_angle_left_2001.png.webp?itok=aUKmGPXB 1x, /sites/axis/files/styles/square_160x160_white/public/2022-09/p3935lr_ceiling_angle_left_2001.png.webp?itok=k7qzzMqQ 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2022-09/p3935lr_ceiling_angle_left_2001.png.webp?itok=k7qzzMqQ" alt="AXIS P3935-LR , viewed from its left angle">

  </picture>



</div>

  <div class="nav-card__text">
    
        <h4>AXIS P39 Dome Camera Series</h4>
        
    <span class="nav-card__product-count">
      4 Products
    </span>
    
      <span class="nav-card__tagline">High-performance domes for onboard surveillance</span>
  
  </div>
</a>
  <a href="/en-us/products/axis-p9117-pv" data-history-node-id="54368" class="nav-card nav-card--single">
    <div class="nav-card__media">
              <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-02/91252.png.webp?itok=vpjLI07X 1x, /sites/axis/files/styles/square_300x300_white/public/2024-02/91252.png.webp?itok=Zg0_R6Jc 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-02/91252.png.webp?itok=vpjLI07X 1x, /sites/axis/files/styles/square_300x300_white/public/2024-02/91252.png.webp?itok=Zg0_R6Jc 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2024-02/91252.png.webp?itok=vpjLI07X 1x, /sites/axis/files/styles/square_300x300_white/public/2024-02/91252.png.webp?itok=Zg0_R6Jc 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2024-02/91252.png.webp?itok=YvJGClke 1x, /sites/axis/files/styles/square_160x160_white/public/2024-02/91252.png.webp?itok=vpjLI07X 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2024-02/91252.png.webp?itok=YvJGClke 1x, /sites/axis/files/styles/square_160x160_white/public/2024-02/91252.png.webp?itok=vpjLI07X 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2024-02/91252.png.webp?itok=vpjLI07X" alt="AXIS P9117-PV Corner Camera  ">

  </picture>




    </div>
        <div class="nav-card__text">
      
              <h4>AXIS P9117-PV Corner Camera</h4>
            
      
      <span class="nav-card__tagline">6 MP corner camera with no blind spots</span>
  
    </div>
  </a>
<a href="/en-us/products/axis-q35-series" data-history-node-id="397" class="nav-card nav-card--deck">
  
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-04/q3548lve_wall_angle_left_2411_Productimageswithcropping%20%281%29.png.webp?itok=myGarVMY 1x, /sites/axis/files/styles/square_300x300_white/public/2025-04/q3548lve_wall_angle_left_2411_Productimageswithcropping%20%281%29.png.webp?itok=dXCArtCm 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-04/q3548lve_wall_angle_left_2411_Productimageswithcropping%20%281%29.png.webp?itok=myGarVMY 1x, /sites/axis/files/styles/square_300x300_white/public/2025-04/q3548lve_wall_angle_left_2411_Productimageswithcropping%20%281%29.png.webp?itok=dXCArtCm 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2025-04/q3548lve_wall_angle_left_2411_Productimageswithcropping%20%281%29.png.webp?itok=myGarVMY 1x, /sites/axis/files/styles/square_300x300_white/public/2025-04/q3548lve_wall_angle_left_2411_Productimageswithcropping%20%281%29.png.webp?itok=dXCArtCm 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2025-04/q3548lve_wall_angle_left_2411_Productimageswithcropping%20%281%29.png.webp?itok=Jzo7NeYy 1x, /sites/axis/files/styles/square_160x160_white/public/2025-04/q3548lve_wall_angle_left_2411_Productimageswithcropping%20%281%29.png.webp?itok=myGarVMY 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2025-04/q3548lve_wall_angle_left_2411_Productimageswithcropping%20%281%29.png.webp?itok=Jzo7NeYy 1x, /sites/axis/files/styles/square_160x160_white/public/2025-04/q3548lve_wall_angle_left_2411_Productimageswithcropping%20%281%29.png.webp?itok=myGarVMY 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2025-04/q3548lve_wall_angle_left_2411_Productimageswithcropping%20%281%29.png.webp?itok=myGarVMY" alt="AXIS Q3548-LVE">

  </picture>



</div>

  <div class="nav-card__text">
    
        <h4>AXIS Q35 Dome Camera Series</h4>
        
    <span class="nav-card__product-count">
      7 Products
    </span>
    
      <span class="nav-card__tagline">AI-powered domes with unmatched performance</span>
  
  </div>
</a>
<a href="/en-us/products/axis-q36-series" data-history-node-id="399" class="nav-card nav-card--deck">
  
  <div class="nav-card__media">        <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-03/q3628ve_tq3810e_wall_angle_left_2303-Productimage_0.png.webp?itok=8XiFCWV8 1x, /sites/axis/files/styles/square_300x300_white/public/2023-03/q3628ve_tq3810e_wall_angle_left_2303-Productimage_0.png.webp?itok=zS8cXEPn 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-03/q3628ve_tq3810e_wall_angle_left_2303-Productimage_0.png.webp?itok=8XiFCWV8 1x, /sites/axis/files/styles/square_300x300_white/public/2023-03/q3628ve_tq3810e_wall_angle_left_2303-Productimage_0.png.webp?itok=zS8cXEPn 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-03/q3628ve_tq3810e_wall_angle_left_2303-Productimage_0.png.webp?itok=8XiFCWV8 1x, /sites/axis/files/styles/square_300x300_white/public/2023-03/q3628ve_tq3810e_wall_angle_left_2303-Productimage_0.png.webp?itok=zS8cXEPn 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2023-03/q3628ve_tq3810e_wall_angle_left_2303-Productimage_0.png.webp?itok=S42NtPHg 1x, /sites/axis/files/styles/square_160x160_white/public/2023-03/q3628ve_tq3810e_wall_angle_left_2303-Productimage_0.png.webp?itok=8XiFCWV8 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2023-03/q3628ve_tq3810e_wall_angle_left_2303-Productimage_0.png.webp?itok=S42NtPHg 1x, /sites/axis/files/styles/square_160x160_white/public/2023-03/q3628ve_tq3810e_wall_angle_left_2303-Productimage_0.png.webp?itok=8XiFCWV8 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2023-03/q3628ve_tq3810e_wall_angle_left_2303-Productimage_0.png.webp?itok=8XiFCWV8" alt="AXIS Q3628-VE Dome Camera">

  </picture>



</div>

  <div class="nav-card__text">
    
        <h4>AXIS Q36 Dome Camera Series</h4>
        
    <span class="nav-card__product-count">
      2 Products
    </span>
    
      <span class="nav-card__tagline">Advanced domes with remote adjustment</span>
  
  </div>
</a>
  <a href="/en-us/products/axis-q9216-slv" data-history-node-id="2575" class="nav-card nav-card--single">
    <div class="nav-card__media">
              <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2020-04/q9216slv_stainless_steel_angle_left_2001.png.webp?itok=SLD7anfz 1x, /sites/axis/files/styles/square_300x300_white/public/2020-04/q9216slv_stainless_steel_angle_left_2001.png.webp?itok=cXvKLJew 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2020-04/q9216slv_stainless_steel_angle_left_2001.png.webp?itok=SLD7anfz 1x, /sites/axis/files/styles/square_300x300_white/public/2020-04/q9216slv_stainless_steel_angle_left_2001.png.webp?itok=cXvKLJew 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2020-04/q9216slv_stainless_steel_angle_left_2001.png.webp?itok=SLD7anfz 1x, /sites/axis/files/styles/square_300x300_white/public/2020-04/q9216slv_stainless_steel_angle_left_2001.png.webp?itok=cXvKLJew 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2020-04/q9216slv_stainless_steel_angle_left_2001.png.webp?itok=XG3BKcaB 1x, /sites/axis/files/styles/square_160x160_white/public/2020-04/q9216slv_stainless_steel_angle_left_2001.png.webp?itok=SLD7anfz 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2020-04/q9216slv_stainless_steel_angle_left_2001.png.webp?itok=XG3BKcaB 1x, /sites/axis/files/styles/square_160x160_white/public/2020-04/q9216slv_stainless_steel_angle_left_2001.png.webp?itok=SLD7anfz 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2020-04/q9216slv_stainless_steel_angle_left_2001.png.webp?itok=SLD7anfz" alt="AXIS Q9216-SLV in stainless steel, from the left angle">

  </picture>




    </div>
        <div class="nav-card__text">
      
              <h4>AXIS Q9216-SLV Network Camera</h4>
            
      
      <span class="nav-card__tagline">Impact-resistant anti-ligature camera</span>
  
    </div>
  </a>
  <a href="/en-us/products/axis-q9307-lv" data-history-node-id="54023" class="nav-card nav-card--single">
    <div class="nav-card__media">
              <picture>
                  <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-12/q9307_wall_angle_left_red_green_led_2312-Productimageswithcropping.png.webp?itok=UBMvjOFv 1x, /sites/axis/files/styles/square_300x300_white/public/2023-12/q9307_wall_angle_left_red_green_led_2312-Productimageswithcropping.png.webp?itok=e1fG8Wv9 2x" media="(min-width: 1360px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-12/q9307_wall_angle_left_red_green_led_2312-Productimageswithcropping.png.webp?itok=UBMvjOFv 1x, /sites/axis/files/styles/square_300x300_white/public/2023-12/q9307_wall_angle_left_red_green_led_2312-Productimageswithcropping.png.webp?itok=e1fG8Wv9 2x" media="(min-width: 1024px) and (max-width: 1359px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_160x160_white/public/2023-12/q9307_wall_angle_left_red_green_led_2312-Productimageswithcropping.png.webp?itok=UBMvjOFv 1x, /sites/axis/files/styles/square_300x300_white/public/2023-12/q9307_wall_angle_left_red_green_led_2312-Productimageswithcropping.png.webp?itok=e1fG8Wv9 2x" media="(min-width: 768px) and (max-width: 1023px)" type="image/webp" width="160" height="160">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2023-12/q9307_wall_angle_left_red_green_led_2312-Productimageswithcropping.png.webp?itok=8xULXfhA 1x, /sites/axis/files/styles/square_160x160_white/public/2023-12/q9307_wall_angle_left_red_green_led_2312-Productimageswithcropping.png.webp?itok=UBMvjOFv 2x" media="(min-width: 576px) and (max-width: 767px)" type="image/webp" width="80" height="80">
              <source srcset="/sites/axis/files/styles/square_80x80_white/public/2023-12/q9307_wall_angle_left_red_green_led_2312-Productimageswithcropping.png.webp?itok=8xULXfhA 1x, /sites/axis/files/styles/square_160x160_white/public/2023-12/q9307_wall_angle_left_red_green_led_2312-Productimageswithcropping.png.webp?itok=UBMvjOFv 2x" media="(max-width: 575px)" type="image/webp" width="80" height="80">
                  <img loading="eager" width="160" height="160" src="/sites/axis/files/styles/square_160x160_white/public/2023-12/q9307_wall_angle_left_red_green_led_2312-Productimageswithcropping.png.webp?itok=UBMvjOFv" alt="AXIS Q9307-LV Dome Camera, viewed from its left angle">

  </picture>




    </div>
        <div class="nav-card__text">
      
              <h4>AXIS Q9307-LV Dome Camera</h4>
            
      
      <span class="nav-card__tagline">All-in-one audio-visual monitoring device</span>
  
    </div>
  </a>

    </div>
  





</div>
```
Then you can go into a series page like "AXIS M3057-PLR Mk II Dome Camera"

   - ➤ Product pages (e.g.):  
     `https://www.axis.com/en-us/products/axis-m3057-plr-mk-ii`

3. **For each product page**:
   - Visit its `/support` page  
     (e.g. `https://www.axis.com/en-us/products/axis-m3057-plr-mk-ii/support`)
   - Find the **Datasheet PDF** download link by grabing the link from this html
```html
<li class="item-list downloads-list__category">
            <h2 class="no-padding-bottom" data-gtm-vis-first-on-screen31532331_296="77256" data-gtm-vis-total-visible-time31532331_296="3000" data-gtm-vis-recent-on-screen31532331_296="78677" data-gtm-vis-has-fired31532331_296="1">Datasheet</h2>
            <input type="checkbox" class="downloads-list__checkbox" aria-label="Toggle category visibility" title="Show or hide this section">
            <hr>
            <ul class="downloads-list__category-items-list">
                                    <li class="downloads-list__list-item">
    <div class="downloads-list__list-item-data">
        <span class="downloads-list__download-title">
            <div>AXIS M3057-PLR Mk II Dome Camera</div>
      </span>
        <span class="downloads-list__download-size-lang">
            <span class="downloads-list__download-size">(pdf) 1.35 MB</span>
        </span>
    </div>
          <div class="download-wrapper">
    <span data-myaxis-access="offline myaxis" class="download-wrapper__partner-requirement"></span>
    <a href="https://www.axis.com/dam/public/28/40/34/datasheet-axis-m3057-plr-mk-ii-dome-camera-en-US-487290.pdf" class="downloads-list__download-button button-action button-action--primary" target="_blank">Download</a>
    
    
  </div>

</li>

                            </ul>
        </li>
```
the link to download the pdf from would be "https://www.axis.com/dam/public/28/40/34/datasheet-axis-m3057-plr-mk-ii-dome-camera-en-US-487290.pdf"
---

### 📄 HTML Structure Example (for PDF location)
```html
<li class="item-list downloads-list__category">
            <h2 class="no-padding-bottom" data-gtm-vis-recent-on-screen31532331_296="789" data-gtm-vis-first-on-screen31532331_296="789" data-gtm-vis-total-visible-time31532331_296="3000" data-gtm-vis-has-fired31532331_296="1">Datasheet</h2>
            <input type="checkbox" class="downloads-list__checkbox" aria-label="Toggle category visibility" title="Show or hide this section">
            <hr>
            <ul class="downloads-list__category-items-list">
                                    <li class="downloads-list__list-item">
    <div class="downloads-list__list-item-data">
        <span class="downloads-list__download-title">
            <div>AXIS M1055-L Box Camera</div>
      </span>
        <span class="downloads-list__download-size-lang">
            <span class="downloads-list__download-size">(pdf) 2.03 MB</span>
        </span>
    </div>
          <div class="download-wrapper">
    <span data-myaxis-access="offline myaxis" class="download-wrapper__partner-requirement"></span>
    <a href="https://www.axis.com/dam/public/9b/cd/13/datasheet-axis-m1055-l-box-camera-en-US-487307.pdf" class="downloads-list__download-button button-action button-action--primary" target="_blank">Download</a>
    
    
  </div>

</li>

                            </ul>
        </li>
```

---

### 📥 PDF Parsing
Download the PDF, then extract the following:

- **SoC Model** (e.g., `ARTPEC-8`)
- **Memory** (e.g., `2 GB RAM`)

Use `PyMuPDF` or `pdfplumber`.

---

### 🧾 Output Format
Return a JSON/dict per product:

```json
{
  "product": "AXIS M1055-L",
  "datasheet_url": "https://...",
  "soc_model": "ARTPEC-8",
  "memory": "2 GB RAM"
}
```

---

### 🔧 Tech Notes
- Use `requests` + `BeautifulSoup` for scraping.
- Respect the hierarchy.
- Skip products with no datasheet.
- Add retry/backoff logic for failed requests.
