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

export const HtmlCssJs = () => (
  <Root>
    <Center>
      <Title mb={"15%"}>Arroz com feijão da web</Title>
      <ImgCenter>
        <Img src={"./img/web.png"}  width={600} height={300}  /> 
      </ImgCenter>
    </Center>
  </Root>
);
