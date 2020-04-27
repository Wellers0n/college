import React from 'react';
import styled from 'styled-components'
import { space, width, fontSize, color } from 'styled-system';

import { Root } from './Intro';

const Img = styled.img`
  ${width}
`;

export const Center = styled.div`
  display: flex;
  flex: 1;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

const Title = styled.span`
  font-size: 50px;
  ${space}
`;

const Subtitle = styled.span`
  font-size: 40px;
  color: #FDAA4C;
  ${space}
`;

const MeName = styled.span`
  font-size: 30px;
  color: #57ad50;
  ${space} 
`;

const ImgCenter = styled.div`
  display: flex;
`



export const Me = () => (
  <Root>
    <Center>
      <Title mt={20} mb={20}>Quem é você mesmo ?</Title>
      <ImgCenter>
        <MeImg src={"./img/meImage.png"} /> 
      </ImgCenter>
    </Center>
  </Root>
);

const MeImg = styled.img`
  max-width: 500px;
  max-height: 500px; 
  border-radius: 30%
`;