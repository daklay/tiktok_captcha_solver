import React, { useState } from "react";
import Slider from "@material-ui/core/Slider";

const PuzzleSlider = () => {
  const [rotation, setRotation] = useState([0, 178.378]);
  const [questions, setQuestions] = useState({
    url1:"https://p19-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/3ca8c42c84c64c56a7e2433415a46884~tplv-b4yrtqhy5a-2.jpeg",
    url2:"https://p19-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/29731ad2885749e3a6ca130d348e145d~tplv-b4yrtqhy5a-2.jpeg",
  });
  const url = "https://www-useast1a.tiktok.com/captcha/get?lang=en&app_name=&h5_sdk_version=2.32.6&h5_sdk_use_type=cdn&sdk_version=3.8.9&iid=0&did=7326160832088393221&device_id=7326160832088393221&ch=web_text&aid=1459&os_type=3&mode=whirl&tmp=1705769793022&platform=h5&webdriver=false&fp=verify_lrm2ckuw_nCtU9Z4F_H9Qp_4NVB_9s7O_dVJFhYfjyQXn&type=verify&detail=jMLGb2roLVO2REV8E-1HPxL2L2o0b9lBX47fu1aKnsmaOE5Zau4aOacNUjt8hDORKR1N7nYz7CDK7FVtnXePulse-54vz8iItKzAcZ3Mcgwh9JJf97JoKldwo34oDUCtldygy7OG4nPO5z7WP1E8f3h1ktgHjp8DvSxlPqffHUv81u95ZKaRnw0dO9acTDcMLX5HfOdcdJR5T-*AnOKZcW77ocr6FoCxkFbD0a-dVs03RlNKFpF7HmQdUTl3LIiDwvT94ka2BP51PuVJg-b2QVpINqip1v-xKVqmdh283lq-IiRpTM9WIYE8HutySdCyc1RcuGS0vzqNjnD7RzZs5FEEBTcXO3gMfqNgwzD*nZXCIZMLAcwgDxX39G5CGfTbPNOidKMKSA7L5W6dyP*liIMQGstaVhqACh*bZxqpbUCE2nBAkZ1sESjDLQLWxetJVrFT4OrCs5C04rBiZchi2hPMfM8w1*dyjUrUEOICuf6i6igubg..&server_sdk_env=%7B%22idc%22:%22maliva%22,%22region%22:%22MALIVA%22,%22server_type%22:%22passport%22%7D&subtype=whirl&challenge_code=99996&os_name=windows&h5_check_version=3.8.9&region=va&triggered_region=va&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=en-US&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F114.0.0.0+Safari%2F537.36+Edg%2F114.0.1823.43&msToken=sx_sT6ze9SO5QzGuTLyhn_66I7PZEB_PxZR5FdQXzC9o_xf0O24Zo5GZWYeYUgCBy18t21urQXHIroxbqGzY5C-BE911573s7fXBUk6xLTSCeJybXaEdnW0JT2ge1g==&X-Bogus=DFSzKIVLAhJANHtetiSeBz9WcBn/&_signature=_02B4Z6wo00001tXM51AAAIDC1cznUAN-huLVzuPAANDl8b"
//   function fetch_imgs()
//   {
//     fetch(url)
//     .then((res)=>res.json())
//     .then((json)=>{setQuestions(({url1:json.data.question.url1, url2:json.data.question.url2}))})
//   }
//   useState(()=>{
//     fetch_imgs();
//   },[])
//   const handleSliderChange = (e) => {
//     const newRotation = e.target.value;
//     setRotation(newRotation);
//   };
  const saveRotationDegree = () => {
    const degree = rotation[0];
    console.log(degree);
    alert("test");
    // fetch_imgs();
  };

  return (
    <>
    <div style={{ position: "relative", width: "fit-content", margin: "auto" }}>
        {/* outer img*/}
      <img
        src={questions.url1}
        alt="Outer Puzzle"
        style={{
          position: "relative",
          borderRadius: "50%",
          height: "700px",
          display: "block",
          transform: `rotate(${-rotation[0]}deg)`,
        }}
      />
      {/* inner img */}
      <img
        src={questions.url2}
        alt="Inner Puzzle"
        style={{
          position: "absolute",
          top: "50%", 
          left: "50%",
          height: "60%",
          borderRadius: "50%",
          transform: `translate(-50%, -50%) rotate(${rotation[0]}deg)`,
          pointerEvents: "none",
        }}
      />
    </div>
    {/* <div>
        <input
          type="range"
          min="0"
          max="178.378"
          step="0.0001"
          value={rotation[0]}
          onChange={handleSliderChange}
          style={{ width: "100%", marginTop: "10px" }} // Added margin for spacing
        />
        <button id="saveButton" onClick={saveRotationDegree}>Save Degree</button>
        <p id="deg">{rotation[0]}</p>
    </div> */}
    <div>
        <div>
          <Slider
            step={0.0001}
            min={0}
            max={178.378}
            value={rotation}
            onChange={(ev, v) => setRotation(v)}
            valueLabelDisplay="off"
            aria-labelledby="range-slider"
          />
        <button id="saveButton" onClick={saveRotationDegree}>Save Degree</button>
        </div>
          <div>{rotation[0]}</div>
          <div>{rotation[1]}</div>
      </div>
    </>
  );
};

export default PuzzleSlider;
