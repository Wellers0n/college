import React from 'react';
import styled from 'styled-components'
import { space, width, fontSize, color } from 'styled-system';

const Img = styled.img`
  ${width}
`;

const Center = styled.div`
  display: flex;
  flex: 1;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

const Root = styled.div([], {
    width: '50vw',
    height: '100vh',
    display: 'flex',
    
});

const Title = styled.span`
  font-size: 50px;
  ${space}
`;


const ImgCenter = styled.div`
  display: flex;
`



export const GoReact = () => (
  <Root>
    <Center>
      <Title mb={20}>ReactJS</Title>
      <ImgCenter>
        <Img src={"./img/react.png"} width={300} height={300}/>
      </ImgCenter>
    </Center>
  </Root>
);
