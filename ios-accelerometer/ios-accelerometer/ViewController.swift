//
//  ViewController.swift
//  ios-accelerometer
//
//  Created by Robin Lin on 2020-10-14.
//

import UIKit
import CoreMotion

class ViewController: UIViewController {

    
    @IBOutlet weak var xAccel: UITextField!
    
    @IBOutlet weak var yAccel: UITextField!
    
    @IBOutlet weak var zAccel: UITextField!
    
    @IBOutlet weak var xGyro: UITextField!
    
    @IBOutlet weak var yGyro: UITextField!
    
    @IBOutlet weak var zGyro: UITextField!
    
    var motion = CMMotionManager()
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        myAcceleromter()
        myGyro()
    }
    var accx = [Double]()
    var accy = [Double]()
    var accz = [Double]()
    var rotx = [Double]()
    var roty = [Double]()
    var rotz = [Double]()
    
    func myAcceleromter() {
        
        motion.accelerometerUpdateInterval = 0.001 // 1/1000 Second Delta t
        motion.startAccelerometerUpdates(to: OperationQueue.current!) {(data,error) in
            if let trueData = data {
                self.view.reloadInputViews()
                let x = trueData.acceleration.x
                let y = trueData.acceleration.y
                let z = trueData.acceleration.z
                self.xAccel.text = "X: \(Double(x))"
                self.yAccel.text = "Y: \(Double(y))"
                self.zAccel.text = "Z: \(Double(z))"
                self.accx.append(x)
                self.accy.append(y)
                self.accz.append(z)
                print("############X-Acceleration############")
                print(self.accx)
                print("############Y-Acceleration############")
                print(self.accy)
                print("############Z-Acceleration############")
                print(self.accz)
            }
        }
    }
    
    func myGyro() {
        motion.gyroUpdateInterval = 0.001 // 1/1000 Second Delta t
        motion.startGyroUpdates(to: OperationQueue.current!) {(data,error) in print(data as Any)
            if let trueData = data {
                self.view.reloadInputViews()
                let x = trueData.rotationRate.x
                let y = trueData.rotationRate.y
                let z = trueData.rotationRate.z
                self.xGyro.text = "X: \(Double(x))"
                self.yGyro.text = "Y: \(Double(y))"
                self.zGyro.text = "Z: \(Double(z))"
                self.rotx.append(x)
                self.roty.append(y)
                self.rotz.append(z)
                print("############X-Rot############")
                print(self.rotx)
                print("############Y-Rot############")
                print(self.roty)
                print("############Z-Rot############")
                print(self.rotz)
            }
        }
    }
}

